import pytest

from airline_operations_intelligence.scenarios.network import (
    build_synthetic_network,
)
from airline_operations_intelligence.scenarios.simulation import (
    simulate_network,
)


@pytest.fixture
def flights():
    return build_synthetic_network()


def test_multi_aircraft_delay_propagation(flights):
    results = simulate_network(
        flights,
        {
            "N101AI": 60,
            "N102AI": 30,
            "N103AI": 90,
        },
    )

    actual = {result.flight_number: result.delay_minutes for result in results}

    assert actual == {
        "AI101": 60,
        "AI102": 45,
        "AI103": 30,
        "AI201": 30,
        "AI202": 15,
        "AI203": 0,
        "AI301": 90,
        "AI302": 75,
        "AI303": 60,
    }


def test_missing_initial_delays_default_to_zero(flights):
    results = simulate_network(flights, {"N101AI": 60})

    delays = {result.flight_number: result.delay_minutes for result in results}

    assert delays["AI101"] == 60
    assert delays["AI201"] == 0
    assert delays["AI301"] == 0


def test_unknown_aircraft_is_rejected(flights):
    with pytest.raises(ValueError, match="Unknown aircraft"):
        simulate_network(flights, {"UNKNOWN": 60})


def test_negative_delay_is_rejected(flights):
    with pytest.raises(ValueError, match="Initial delay cannot be negative"):
        simulate_network(flights, {"N101AI": -10})


def test_simulation_is_deterministic(flights):
    initial_delays = {
        "N101AI": 60,
        "N102AI": 30,
        "N103AI": 90,
    }

    first = simulate_network(flights, initial_delays)
    second = simulate_network(flights, initial_delays)

    assert first == second


def test_simulation_returns_all_flights(flights):
    results = simulate_network(flights, {})

    assert len(results) == len(flights)
    assert len({r.flight_number for r in results}) == 9
