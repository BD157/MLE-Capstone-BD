# End-to-End ML Capstone 
## Genome Clustering & Variant Classification

A scalable API for SARS-CoV-2 genome clustering and variant classification that transitions from experimental notebooks to a production-ready FastAPI service. The system supports containerized deployment and is designed with automated CI/CD pipelines in mind, making it reproducible and cloud-deployable.
This project aims to support lineage-based clustering for public health analysis, while focusing on practical ML engineering concerns such as turning notebook-based experiments into reusable code, organizing logic so it can be maintained over time, and making the system easier to run in real environments.

## Summary

Many machine learning projects stall at exploratory notebooks and never mature into deployable systems. This repository demonstrates how genome-based ML workflows can evolve from research code into a structured, service-oriented application suitable for production environments.
The focus is as much on **engineering discipline** as on modeling, showing how to move from analysis to inference with scalability and maintainability in mind.

---

**Core goals:**
- Build an end-to-end machine learning project, from data analysis to model inference
- Move work out of notebooks into reusable, maintainable code
- Expose clustering and classification through a runnable API
- Set up to later support testing, automation, and deployment

## Problem Statement

In practice, genomic surveillance work is often done using one-off scripts and exploratory notebooks. These approaches work for analysis, but they are difficult
to reproduce, hard to scale, and not designed to be reused by others. This project aims to turn SARS-CoV-2 genome clustering and variant classification into a reusable service, so the same analysis can be run consistently, shared across teams, and deployed in real environments.

---

## Project Scope

### Implemented
- Code for clustering genome sequences and classifying variants
- A FastAPI service for running model inference
- Support for running locally and with Docker
- Basic service endpoints, including a health check
- An optional Streamlit UI for interacting with the API

### Planned Extensions
- Move more model and data logic into reusable Python modules
- Add basic tests and automation
- Improve model evaluation and result reporting
- Track model and data changes over time
- Make deployment and updates more robust

---

## Repository Structure

## Local Setup

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```
After running, the API will be available at:

http://localhost:8000

## Docker

```bash
docker build -t genome-api .
docker run -p 8000:8000 genome-api
```
This enables consistent, reproducible execution across environments.

## API Endpoints (Hosted via Render)

The service exposes the following endpoints:

GET /health
Health check for service readiness
POST /cluster
Cluster genome sequences
POST /classify
Classify genome sequences into variants
Interactive API documentation is available via:
/docs (Swagger UI)
/redoc (ReDoc)

## Streamlit

Update streamlit_app/app.py with your Render API URL and deploy on Streamlit Cloud.

---

## Engineering Focus

This project emphasizes:
- Clear separation between research and inference code
- Reproducibility and environment consistency
- Incremental progression toward production ML systems
- Maintainability over one-off experimentation

## Future Work

- Move remaining model logic out of notebooks and into `src/`
- Add unit tests and basic integration tests
- Set up continuous integration for automated checks
- Expand evaluation metrics and result reporting
- Improve how models are versioned and managed over time


## Author

Built and maintained by BD as part of a machine learning engineering capstone project.
