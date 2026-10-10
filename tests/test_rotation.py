from datetime import UTC, datetime

import pytest

from airline_operations_intelligence.domain.models import (
    Aircraft,
    Airport,
    Flight,
)
from airline_operations_intelligence.domain.rotation import (
    propagate_delay,
)


@pytest.fixture
def rotation():
    dal = Airport("DAL", "Dallas Love Field")
    hou = Airport("HOU", "Houston Hobby")
    sat = Airport("SAT", "San Antonio")

    aircraft = Aircraft("N100AI", "B737-800")

    def flight(number, origin, destination, dep, arr):
        return Flight(
            flight_number=number,
            aircraft=aircraft,
            origin=origin,
            destination=destination,
            scheduled_departure=datetime(2026, 10, 10, dep // 60, dep % 60, tzinfo=UTC),
            scheduled_arrival=datetime(2026, 10, 10, arr // 60, arr % 60, tzinfo=UTC),
        )

    return [
        flight("AI101", dal, hou, 480, 540),
        flight("AI102", hou, sat, 585, 640),
        flight("AI103", sat, dal, 685, 750),
    ]


def test_delay_propagation(rotation):
    results = propagate_delay(rotation, 60)

    assert [r.delay_minutes for r in results] == [60, 45, 30]


def test_no_delay(rotation):
    results = propagate_delay(rotation, 0)

    assert [r.delay_minutes for r in results] == [0, 0, 0]


def test_large_delay(rotation):
    results = propagate_delay(rotation, 120)

    assert [r.delay_minutes for r in results] == [120, 105, 90]


def test_negative_delay_rejected(rotation):
    with pytest.raises(ValueError):
        propagate_delay(rotation, -10)


def test_custom_minimum_turnaround(rotation):
    results = propagate_delay(
        rotation,
        initial_arrival_delay_minutes=60,
        minimum_turnaround_minutes=20,
    )

    assert [r.delay_minutes for r in results] == [60, 35, 10]


def test_negative_turnaround_rejected(rotation):
    with pytest.raises(ValueError):
        propagate_delay(
            rotation,
            initial_arrival_delay_minutes=60,
            minimum_turnaround_minutes=-5,
        )


def test_zero_turnaround_requirement(rotation):
    results = propagate_delay(
        rotation,
        initial_arrival_delay_minutes=60,
        minimum_turnaround_minutes=0,
    )

    assert [r.delay_minutes for r in results] == [60, 15, 0]
