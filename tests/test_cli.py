import csv
import subprocess
import sys

from airline_operations_intelligence.scenarios.run import main


def read_rows(path):
    with path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def test_cli_generates_default_scenario(tmp_path, monkeypatch):
    output = tmp_path / "default"

    monkeypatch.setattr(
        sys,
        "argv",
        ["run", "--output-dir", str(output)],
    )

    main()

    flights = read_rows(output / "flights.csv")
    delays = read_rows(output / "delays.csv")

    assert len(flights) == 9
    assert len(delays) == 9


def test_cli_supports_custom_delays(tmp_path, monkeypatch):
    output = tmp_path / "severe"

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "run",
            "--output-dir",
            str(output),
            "--delay-a",
            "120",
            "--delay-b",
            "45",
            "--delay-c",
            "180",
        ],
    )

    main()

    delays = {
        row["flight_number"]: int(row["delay_minutes"])
        for row in read_rows(output / "delays.csv")
    }

    assert delays["AI101"] == 120
    assert delays["AI201"] == 45
    assert delays["AI301"] == 180


def test_cli_runs_as_python_module(tmp_path):
    output = tmp_path / "module"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "airline_operations_intelligence.scenarios.run",
            "--output-dir",
            str(output),
        ],
        capture_output=True,
        text=True,
        check=True,
    )

    assert "Generated 9 flights and 9 delay records." in result.stdout
    assert (output / "flights.csv").exists()
    assert (output / "delays.csv").exists()
