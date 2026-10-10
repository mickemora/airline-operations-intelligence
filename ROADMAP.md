# Development Roadmap

This roadmap describes **planned milestones**, not deployed capabilities. Status is updated only after code, tests, and documentation are verified.

| Milestone | Focus | Status | Demonstrable deliverable |
| --- | --- | --- | --- |
| V1.1 | Airline domain model and delay propagation | Local implementation committed; publication pending | Python domain classes, deterministic propagation, eight reported passing tests |
| V1.2 | Operational realism and synthetic scenarios | Planned | Minimum turnaround variations, edge-case validation, multi-aircraft fixtures, reproducible CLI |
| V2 | Databricks Lakehouse | Planned | Bronze/Silver/Gold Delta pipelines and synthetic data quality checks |
| V3 | Unity Catalog | Planned | Catalog design, permissions, classifications, and lineage evidence |
| V4 | Amazon Neptune | Planned | Graph schema, graph ingestion, and multi-hop dependency queries |
| V5 | Governed graph integration | Planned | Databricks-to-Neptune export, incremental updates, and security boundary tests |
| V6 | Bedrock agentic investigator | Planned | Bounded tool calls, evidence-grounded responses, and evaluation harness |
| V7 | Recovery decision support | Planned | Feasibility checks, scenario comparisons, human approval boundary |
| V8 | Enterprise hardening | Planned | CI/CD, observability, threat model, cost analysis, and architecture review |

## V1.1 — Acceptance criteria

- [x] Model airport, aircraft, and scheduled flight entities
- [x] Calculate scheduled flight duration
- [x] Propagate delays through one ordered aircraft rotation
- [x] Enforce aircraft/airport continuity and reject overlapping schedules
- [x] Support configurable synthetic minimum turnaround
- [x] Report eight passing unit tests and clean lint/format checks
- [ ] Publish implementation to remote feature branch
- [ ] Review and merge pull request into `main`

## Architectural guardrails

1. Use synthetic or appropriately licensed public data only; no airline proprietary or passenger-identifiable records.
2. Clearly separate actual implementation from aspirational architecture.
3. Use UTC-aware timestamps and explicitly document schedule and turnaround assumptions.
4. Treat Unity Catalog and Neptune as separate enforcement domains.
5. Keep recovery actions advisory until deterministic constraints and human approval are implemented.
6. Evaluate correctness, freshness, security, and cost before claiming operational benefits.

## Business evaluation targets (future)

- Accuracy of downstream dependency identification
- Time to identify potentially affected flights
- Precision and recall against synthetic labeled disruption scenarios
- Time to generate feasible recovery alternatives
- Governance policy enforcement and traceability

No operational improvements or airline cost savings are claimed at this stage.
