from collections import defaultdict
from itertools import pairwise

from airline_operations_intelligence.scenarios.network import (
    build_synthetic_network,
)


def test_network_contains_expected_entities():
    flights = build_synthetic_network()

    assert len(flights) == 9
    assert len({f.flight_number for f in flights}) == 9
    assert len({f.aircraft.registration for f in flights}) == 3

    airports = {f.origin.code for f in flights} | {f.destination.code for f in flights}

    assert airports == {"DAL", "HOU", "AUS", "SAT"}


def test_each_aircraft_has_three_flights():
    flights = build_synthetic_network()

    rotations = defaultdict(list)

    for flight in flights:
        rotations[flight.aircraft.registration].append(flight)

    assert len(rotations) == 3
    assert all(len(rotation) == 3 for rotation in rotations.values())


def test_aircraft_rotations_are_connected():
    flights = build_synthetic_network()

    rotations = defaultdict(list)

    for flight in flights:
        rotations[flight.aircraft.registration].append(flight)

    for rotation in rotations.values():
        ordered = sorted(
            rotation,
            key=lambda flight: flight.scheduled_departure,
        )

        for previous, current in pairwise(ordered):
            assert previous.destination == current.origin


def test_aircraft_schedules_do_not_overlap():
    flights = build_synthetic_network()

    rotations = defaultdict(list)

    for flight in flights:
        rotations[flight.aircraft.registration].append(flight)

    for rotation in rotations.values():
        ordered = sorted(
            rotation,
            key=lambda flight: flight.scheduled_departure,
        )

        for previous, current in pairwise(ordered):
            assert current.scheduled_departure >= previous.scheduled_arrival


def test_all_flights_have_positive_duration():
    flights = build_synthetic_network()

    assert all(flight.duration_minutes > 0 for flight in flights)


def test_network_is_reproducible():
    first = build_synthetic_network()
    second = build_synthetic_network()

    assert first == second
