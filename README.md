# Airline Operations Intelligence

**Governed Knowledge Graph & Agentic AI Reference Architecture**

An independent, hands-on enterprise AI engineering project exploring how flight disruptions propagate through aircraft rotations, with a roadmap toward governed lakehouse data, graph-based dependency analysis, and agentic decision support.

> **Disclaimer:** Synthetic educational scenarios inspired by airline operations. This project is not affiliated with or endorsed by Southwest Airlines and does not use proprietary airline operational data. Flight identifiers, schedules, and turnaround requirements are illustrative.

## Business challenge

An aircraft arriving late can delay subsequent flights in its rotation. Understanding the downstream impact requires reliable flight schedules, consistent aircraft assignments, airport continuity, and realistic turnaround constraints. Future versions will examine how this dependency analysis can inform operations recovery decisions.

## Business case and proposed solution

![Airline Operations Intelligence — business case, solution architecture, delay propagation example, and development roadmap](docs/images/Airline%20Operations%20Intelligence%20Roadmap.png)

*Executive overview of the business challenge, proposed enterprise architecture, expected benefits, and phased delivery roadmap. The diagram illustrates the target solution; the Databricks, Neptune, and Bedrock integrations are not yet implemented.*

### Why this matters

An aircraft delay rarely affects only one flight. The same aircraft may be scheduled for several legs, while aircraft availability, airports, gates, crews, and weather create interconnected operational dependencies. Without a unified view of those relationships, operators may struggle to understand downstream effects quickly and evaluate recovery options.

### Proposed approach

1. **Model and simulate operations:** represent aircraft, airports, flights, rotations, and turnaround constraints; calculate how disruptions propagate.
2. **Prepare and govern data:** use **Databricks / Delta Lake** for curated operational datasets and **Unity Catalog** for governance within the Databricks environment.
3. **Analyze dependencies:** use **Amazon Neptune** to represent and traverse relationships among operational entities.
4. **Investigate with AI:** use **Amazon Bedrock / AgentCore** for bounded, evidence-grounded analysis of disruption scenarios.
5. **Support human decisions:** present explainable impacts, options, and trade-offs for operations teams to evaluate.

**Intended business outcomes:** improved disruption visibility, faster and better-informed recovery decisions, greater operational resilience, and opportunities to reduce customer impact and operational costs. These are goals, not validated performance claims.

### Working example — V1.1

In our synthetic three-flight rotation, an initial **60-minute** arrival delay propagates to **45 minutes** on the second flight and **30 minutes** on the third. The example assumes **45 minutes** of scheduled ground time and a **30-minute** minimum turnaround between flights. This deterministic calculation is implemented and tested; it is not a live airline prediction.

## Current implementation — V1.1

**Completed and merged into `main`.** The V1.1 Python implementation, tests, and documentation are available in this repository.

- Immutable Python domain models for airports, aircraft, and scheduled flights
- Flight duration calculation
- Deterministic arrival-delay propagation through an ordered aircraft rotation
- Aircraft and airport continuity checks; overlapping-schedule rejection
- Configurable minimum turnaround time (default: 30 minutes, synthetic assumption)
- Input validation for negative delays and turnaround requirements
- Eight reported passing pytest tests; Ruff linting and formatting checks

**Scope limitations:** V1.1 models a single aircraft rotation, constant flight durations, and arrival delays carried forward from departure delays. It does not yet model crew legality, actual turnaround variability, gate conflicts, aircraft swaps, passenger connections, or network optimization. It is not a production disruption prediction engine.

## Run locally

Requires Python 3.12 and [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/mickemora/airline-operations-intelligence.git
cd airline-operations-intelligence
uv sync
uv run pytest -v
uv run ruff check .
uv run ruff format --check .
```

## Target reference architecture (planned, not deployed)

```text
Synthetic flight / aircraft / airport / maintenance datasets
                          |
                          v
                 Databricks + Delta Lake
                          |
                 Unity Catalog governance
                          |
                Governed export pipeline
                          |
                          v
                 Amazon Neptune graph
                          |
              Bounded graph query service
                          |
                          v
             Amazon Bedrock / AgentCore
                          |
              Explainable disruption analysis
                          |
                 Human decision maker
```

- **Databricks / Delta Lake:** ingestion, curation, and analytics
- **Unity Catalog:** metadata, lineage, access controls, and governed Databricks assets
- **Amazon Neptune:** graph representation and multi-hop dependency traversal
- **Amazon Bedrock / AgentCore:** tool-mediated investigation and explanation
- **AWS security and observability:** IAM, least privilege, logging, and operational monitoring

**Governance boundary:** Unity Catalog does not automatically enforce policies on exported Neptune graph data. Neptune authorization, application-level controls, data minimization, export lineage, and deletion propagation must be designed and tested independently.

## Engineering approach

Each lab will distinguish completed functionality from proposed architecture and will include tests, reproducible commands, architectural decisions, and business implications. See [ROADMAP.md](ROADMAP.md) for planned milestones.

## Repository structure

```text
src/airline_operations_intelligence/
  domain/
    models.py
    rotation.py
tests/
  test_models.py
  test_rotation.py
pyproject.toml
uv.lock
ROADMAP.md
```

## Intended portfolio outcomes

Demonstrate business-led architecture, hands-on Python engineering, enterprise data governance, graph modeling, agentic tool use, and evaluation-driven delivery—without representing synthetic results as real airline performance.
