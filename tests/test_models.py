from datetime import UTC, datetime

from airline_operations_intelligence.domain.models import (
    Aircraft,
    Airport,
    Flight,
)


def test_flight_duration():
    dal = Airport("DAL", "Dallas Love Field")
    hou = Airport("HOU", "Houston Hobby")

    aircraft = Aircraft("N100AI", "B737-800")

    flight = Flight(
        flight_number="AI101",
        aircraft=aircraft,
        origin=dal,
        destination=hou,
        scheduled_departure=datetime(2026, 10, 10, 13, 0, tzinfo=UTC),
        scheduled_arrival=datetime(2026, 10, 10, 14, 0, tzinfo=UTC),
    )

    assert flight.duration_minutes == 60
