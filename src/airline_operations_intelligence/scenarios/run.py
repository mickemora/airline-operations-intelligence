import argparse
from pathlib import Path

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


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate synthetic airline operations data."
    )

    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/generated"),
        help="Directory for generated CSV files.",
    )

    parser.add_argument(
        "--delay-a",
        type=int,
        default=60,
        help="Initial delay for aircraft N101AI.",
    )

    parser.add_argument(
        "--delay-b",
        type=int,
        default=30,
        help="Initial delay for aircraft N102AI.",
    )

    parser.add_argument(
        "--delay-c",
        type=int,
        default=90,
        help="Initial delay for aircraft N103AI.",
    )

    args = parser.parse_args()

    flights = build_synthetic_network()

    initial_delays = {
        "N101AI": args.delay_a,
        "N102AI": args.delay_b,
        "N103AI": args.delay_c,
    }

    results = simulate_network(flights, initial_delays)

    export_flights_csv(
        flights,
        args.output_dir / "flights.csv",
    )

    export_delays_csv(
        results,
        args.output_dir / "delays.csv",
    )

    print(f"Generated {len(flights)} flights and {len(results)} delay records.")
    print(f"Output directory: {args.output_dir}")


if __name__ == "__main__":
    main()
