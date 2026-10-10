# Airline Operations Intelligence

**Governed Knowledge Graph & Agentic AI Reference Architecture**

A hands-on enterprise AI engineering project exploring airline disruption intelligence using synthetic operational data, Databricks Unity Catalog, Amazon Neptune, and AWS Bedrock AgentCore.

> Independent educational reference architecture inspired by airline operations. Not affiliated with Southwest Airlines. No proprietary airline data is used.

## Business problem

Aircraft delays can propagate through flight rotations and operational dependencies. This project develops reproducible models and eventually governed data pipelines, graph analysis, and explainable AI decision support to investigate those disruptions.

## Current status

**V1.1 — Airline Operational Domain Model: In progress.** The repository is initialized; implementation and tests are forthcoming.

## Planned architecture

- **Databricks / Delta Lake:** data preparation and analytics
- **Unity Catalog:** governance and lineage for Databricks assets
- **Amazon Neptune:** operational knowledge graph and relationship traversal
- **Amazon Bedrock / AgentCore:** bounded agentic investigation tools
- **Python / pytest:** synthetic data generation, domain logic, and evaluation

These are planned integrations, not yet implemented. Unity Catalog does not automatically enforce permissions on data copied into Neptune; separate controls will be required.

## Development approach

Incremental, test-driven labs with synthetic datasets, reproducible demonstrations, architecture decisions, and explicit separation between completed and planned capabilities.
