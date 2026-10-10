# Airline Operations Intelligence

**Governed Knowledge Graph & Agentic AI Reference Architecture**

An independent, hands-on enterprise AI engineering project exploring how flight disruptions propagate through aircraft rotations, with a roadmap toward governed lakehouse data, graph-based dependency analysis, and agentic decision support.

> **Disclaimer:** Synthetic educational scenarios inspired by airline operations. This project is not affiliated with or endorsed by Southwest Airlines and does not use proprietary airline operational data. Flight identifiers, schedules, and turnaround requirements are illustrative.

## Business challenge

An aircraft arriving late can delay subsequent flights in its rotation. Understanding the downstream impact requires reliable flight schedules, consistent aircraft assignments, airport continuity, and realistic turnaround constraints. Future versions will examine how this dependency analysis can inform operations recovery decisions.

## Current implementation — V1.1

**Implemented locally and committed by the project author; remote feature-branch publication pending.**

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

> Until V1.1 is merged into `main`, check out `feature/v1.1-airline-domain-model` after cloning (once pushed).

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
