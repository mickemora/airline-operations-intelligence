from datetime import UTC, datetime

from airline_operations_intelligence.domain.models import (
    Aircraft,
    Airport,
    Flight,
)


def build_synthetic_network() -> list[Flight]:
    """Build a reproducible synthetic airline flight network."""

    airports = {
        "DAL": Airport("DAL", "Dallas Love Field"),
        "HOU": Airport("HOU", "Houston Hobby"),
        "AUS": Airport("AUS", "Austin-Bergstrom"),
        "SAT": Airport("SAT", "San Antonio International"),
    }

    aircraft = [
        Aircraft("N101AI", "B737-800"),
        Aircraft("N102AI", "B737-800"),
        Aircraft("N103AI", "B737-800"),
    ]

    def flight(
        number: str,
        plane: Aircraft,
        origin: str,
        destination: str,
        departure_hour: int,
        departure_minute: int,
        arrival_hour: int,
        arrival_minute: int,
    ) -> Flight:
        return Flight(
            flight_number=number,
            aircraft=plane,
            origin=airports[origin],
            destination=airports[destination],
            scheduled_departure=datetime(
                2026,
                10,
                10,
                departure_hour,
                departure_minute,
                tzinfo=UTC,
            ),
            scheduled_arrival=datetime(
                2026,
                10,
                10,
                arrival_hour,
                arrival_minute,
                tzinfo=UTC,
            ),
        )

    return [
        # Aircraft 1: DAL -> HOU -> SAT -> DAL
        flight("AI101", aircraft[0], "DAL", "HOU", 8, 0, 9, 0),
        flight("AI102", aircraft[0], "HOU", "SAT", 9, 45, 10, 40),
        flight("AI103", aircraft[0], "SAT", "DAL", 11, 25, 12, 30),
        # Aircraft 2: HOU -> AUS -> DAL -> HOU
        flight("AI201", aircraft[1], "HOU", "AUS", 8, 15, 9, 10),
        flight("AI202", aircraft[1], "AUS", "DAL", 9, 55, 10, 55),
        flight("AI203", aircraft[1], "DAL", "HOU", 11, 40, 12, 40),
        # Aircraft 3: SAT -> DAL -> HOU -> SAT
        flight("AI301", aircraft[2], "SAT", "DAL", 8, 30, 9, 35),
        flight("AI302", aircraft[2], "DAL", "HOU", 10, 20, 11, 20),
        flight("AI303", aircraft[2], "HOU", "SAT", 12, 5, 13, 0),
    ]
