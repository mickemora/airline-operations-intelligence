import csv

from airline_operations_intelligence.scenarios.export import (
    export_delays_csv,
    export_flights_csv,
)
from airline_operations_intelligence.scenarios.network import (
    build_synthetic_network,
)
from airline_operations_intelligence.scenarios.simulation import (
    simulate_network,
)


def read_csv(path):
    with path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def test_flight_export_contains_all_records(tmp_path):
    flights = build_synthetic_network()
    output = tmp_path / "flights.csv"

    export_flights_csv(flights, output)

    rows = read_csv(output)

    assert len(rows) == 9
    assert {row["flight_number"] for row in rows} == {
        flight.flight_number for flight in flights
    }


def test_flight_export_preserves_schedule(tmp_path):
    flights = build_synthetic_network()
    output = tmp_path / "flights.csv"

    export_flights_csv(flights, output)

    rows = read_csv(output)
    first = rows[0]

    assert first["flight_number"] == "AI101"
    assert first["aircraft_registration"] == "N101AI"
    assert first["origin"] == "DAL"
    assert first["destination"] == "HOU"
    assert first["scheduled_departure"] == "2026-10-10T08:00:00+00:00"
    assert first["scheduled_arrival"] == "2026-10-10T09:00:00+00:00"


def test_delay_export_matches_simulation(tmp_path):
    flights = build_synthetic_network()
    results = simulate_network(
        flights,
        {"N101AI": 60, "N102AI": 30, "N103AI": 90},
    )

    output = tmp_path / "delays.csv"
    export_delays_csv(results, output)

    rows = read_csv(output)
    delays = {row["flight_number"]: int(row["delay_minutes"]) for row in rows}

    assert len(rows) == 9
    assert delays["AI101"] == 60
    assert delays["AI102"] == 45
    assert delays["AI103"] == 30
    assert delays["AI203"] == 0
    assert delays["AI301"] == 90


def test_exports_are_reproducible(tmp_path):
    flights = build_synthetic_network()
    results = simulate_network(flights, {"N101AI": 60})

    first_dir = tmp_path / "first"
    second_dir = tmp_path / "second"

    export_flights_csv(flights, first_dir / "flights.csv")
    export_flights_csv(flights, second_dir / "flights.csv")

    export_delays_csv(results, first_dir / "delays.csv")
    export_delays_csv(results, second_dir / "delays.csv")

    assert (first_dir / "flights.csv").read_bytes() == (
        second_dir / "flights.csv"
    ).read_bytes()

    assert (first_dir / "delays.csv").read_bytes() == (
        second_dir / "delays.csv"
    ).read_bytes()


def test_exports_create_missing_directories(tmp_path):
    flights = build_synthetic_network()
    output = tmp_path / "nested" / "data" / "flights.csv"

    export_flights_csv(flights, output)

    assert output.exists()
    assert len(read_csv(output)) == 9
