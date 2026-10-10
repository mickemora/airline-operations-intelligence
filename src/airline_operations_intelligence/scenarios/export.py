import csv
from pathlib import Path

from airline_operations_intelligence.domain.models import Flight
from airline_operations_intelligence.scenarios.simulation import (
    SimulationResult,
)


def export_flights_csv(
    flights: list[Flight],
    output_path: Path,
) -> None:
    """Export synthetic flight schedules to CSV."""

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(
            [
                "flight_number",
                "aircraft_registration",
                "aircraft_type",
                "origin",
                "destination",
                "scheduled_departure",
                "scheduled_arrival",
            ]
        )

        for flight in sorted(flights, key=lambda f: f.flight_number):
            writer.writerow(
                [
                    flight.flight_number,
                    flight.aircraft.registration,
                    flight.aircraft.aircraft_type,
                    flight.origin.code,
                    flight.destination.code,
                    flight.scheduled_departure.isoformat(),
                    flight.scheduled_arrival.isoformat(),
                ]
            )


def export_delays_csv(
    results: list[SimulationResult],
    output_path: Path,
) -> None:
    """Export simulated flight delays to CSV."""

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(
            [
                "flight_number",
                "aircraft_registration",
                "delay_minutes",
            ]
        )

        for result in sorted(results, key=lambda r: r.flight_number):
            writer.writerow(
                [
                    result.flight_number,
                    result.aircraft_registration,
                    result.delay_minutes,
                ]
            )
