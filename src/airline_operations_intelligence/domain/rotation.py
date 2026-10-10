from dataclasses import dataclass
from itertools import pairwise

from .models import Flight


@dataclass(frozen=True)
class FlightDelay:
    flight_number: str
    delay_minutes: int


def propagate_delay(
    flights: list[Flight],
    initial_arrival_delay_minutes: int,
    minimum_turnaround_minutes: int = 30,
) -> list[FlightDelay]:
    """Propagate aircraft delays with minimum turnaround constraints."""

    if initial_arrival_delay_minutes < 0:
        raise ValueError("Initial delay cannot be negative")

    if minimum_turnaround_minutes < 0:
        raise ValueError("Minimum turnaround cannot be negative")

    if not flights:
        return []

    delays = [
        FlightDelay(
            flights[0].flight_number,
            initial_arrival_delay_minutes,
        )
    ]

    previous_arrival_delay = initial_arrival_delay_minutes

    for previous, current in pairwise(flights):
        if previous.aircraft != current.aircraft:
            raise ValueError("Flights must use the same aircraft")

        if previous.destination != current.origin:
            raise ValueError("Aircraft rotation has disconnected airports")

        if current.scheduled_departure < previous.scheduled_arrival:
            raise ValueError("Flights have overlapping schedules")

        scheduled_turnaround = current.scheduled_departure - previous.scheduled_arrival

        turnaround_minutes = scheduled_turnaround.total_seconds() / 60

        current_delay = max(
            0,
            previous_arrival_delay + minimum_turnaround_minutes - turnaround_minutes,
        )

        delays.append(
            FlightDelay(
                current.flight_number,
                int(current_delay),
            )
        )

        previous_arrival_delay = current_delay

    return delays
