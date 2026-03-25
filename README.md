# YouTube API ELT Pipeline

An end-to-end ELT pipeline that extracts YouTube channel metadata from the YouTube API, loads raw data into PostgreSQL staging tables, transforms it into core analytical layers, and runs through a containerized Airflow-based workflow with testing and data quality checks.

```mermaid
flowchart LR
    A[YouTube API] --> B[Python Extraction]
    B --> C[Raw JSON Data]
    C --> D[Airflow DAGs]
    D --> E[PostgreSQL Staging]
    E --> F[Core Layer]
    F --> G[Soda / pytest Checks]
```

## Overview

This project was built to implement a complete end-to-end ELT workflow using tools and practices commonly seen in production-style data engineering environments. The focus of the project was not only on extracting and loading data, but also on understanding how orchestration, containerization, testing, and data quality checks fit into a more complete pipeline setup.

The pipeline uses the YouTube API as its source, stores raw data in a staging layer, applies transformation logic into a core layer, and prepares the data for downstream querying and analysis.

## Motivation

The main goal of this project was to build a complete ELT implementation around Airflow, Docker, PostgreSQL, and Python while also incorporating workflow components such as orchestration, containerized execution, unit testing, data quality checks, and CI/CD support.

Rather than focusing only on extraction scripts, this project was intended to bring multiple parts of a real pipeline workflow together in one place and strengthen hands-on understanding of how production-style data workflows are structured.

## Dataset

The project uses the YouTube API to pull channel-level video metadata.

Example fields extracted include:

- Video ID
- Video Title
- Upload Date
- Duration
- View Count
- Like Count
- Comment Count

The pipeline can be adapted to other YouTube channels by changing the relevant channel configuration.

## Pipeline Summary

At a high level, the pipeline follows this flow:

1. Python scripts extract raw data from the YouTube API
2. Raw output is loaded into a staging schema in PostgreSQL
3. Transformation logic processes staging data into a core schema
4. Airflow orchestrates the workflow through multiple DAGs
5. Unit tests and data quality checks help validate reliability and data integrity
6. The final dataset becomes ready for downstream analysis and querying

## Tools and Technologies

### Languages
- Python
- SQL

### Orchestration
- Apache Airflow

### Containerization
- Docker
- Docker Compose

### Data Storage
- PostgreSQL

### Testing and Data Quality
- pytest
- Soda Core

### CI/CD
- GitHub Actions

## Workflow Components

### Extraction
The extraction layer connects to the YouTube API and retrieves channel and video metadata using Python-based scripts.

### Staging Load
Raw API data is first loaded into PostgreSQL staging tables to preserve source-level structure before downstream processing.

### Transformation
Transformation logic processes staging-layer data into cleaner core-layer tables intended for analysis and reporting use.

### Orchestration
The workflow is orchestrated through Airflow and organized into separate DAGs for extraction, database updates, and data quality checks.

### Testing and Validation
The project includes:
- unit testing for selected pipeline components
- data quality checks across database layers
- CI/CD support for validating workflow changes

## Airflow DAGs

The pipeline is organized around three main DAGs:

- **produce_json**  
  Pulls data from the YouTube API and produces raw JSON output

- **update_db**  
  Processes the raw data and loads it into staging and core schemas

- **data_quality**  
  Runs quality checks on both layers in the database

## Project Structure

```bash
YT_ELT/
├── .github/
│   └── workflows/
├── dags/
├── data/
├── docker/
│   └── postgres/
├── images/
├── include/
│   └── soda/
├── tests/
├── docker-compose.yaml
├── dockerfile
├── requirements.txt
├── LICENSE
└── README.md

## Attribution

This project was developed through hands-on work based on an instructor-guided project by **Matthew Schembri** and is being used as a foundation for continued learning, refinement, and extension.
