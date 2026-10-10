from collections import defaultdict
from dataclasses import dataclass

from airline_operations_intelligence.domain.models import Flight
from airline_operations_intelligence.domain.rotation import propagate_delay


@dataclass(frozen=True)
class SimulationResult:
    flight_number: str
    aircraft_registration: str
    delay_minutes: int


def simulate_network(
    flights: list[Flight],
    initial_delays: dict[str, int],
    minimum_turnaround_minutes: int = 30,
) -> list[SimulationResult]:
    """Simulate independent aircraft rotations in a flight network."""

    rotations: dict[str, list[Flight]] = defaultdict(list)

    for flight in flights:
        rotations[flight.aircraft.registration].append(flight)

    unknown_aircraft = set(initial_delays) - set(rotations)

    if unknown_aircraft:
        raise ValueError(f"Unknown aircraft registrations: {sorted(unknown_aircraft)}")

    results = []

    for registration, rotation in sorted(rotations.items()):
        ordered = sorted(
            rotation,
            key=lambda flight: flight.scheduled_departure,
        )

        initial_delay = initial_delays.get(registration, 0)

        propagated = propagate_delay(
            ordered,
            initial_arrival_delay_minutes=initial_delay,
            minimum_turnaround_minutes=minimum_turnaround_minutes,
        )

        for flight_delay in propagated:
            results.append(
                SimulationResult(
                    flight_number=flight_delay.flight_number,
                    aircraft_registration=registration,
                    delay_minutes=flight_delay.delay_minutes,
                )
            )

    return results
