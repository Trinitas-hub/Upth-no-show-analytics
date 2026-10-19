# UPTH No-Show Analytics

## Project Overview

This project is an academic healthcare analytics prototype developed to explore the prediction of outpatient appointment no-shows in the context of the University of Port Harcourt Teaching Hospital (UPTH), Rivers State, Nigeria.

The project uses the publicly available Medical Appointment No Shows dataset as a proxy dataset and does not represent a live UPTH production system.

The objective is to demonstrate how machine learning, responsible AI, monitoring, and data visualization can support healthcare decision-making while maintaining human oversight.

## Project Components

The repository includes:

- Data preprocessing and validation
- Logistic Regression and Random Forest modelling
- Model performance evaluation
- Fairness assessment
- Model explainability
- Streamlit analytics dashboard
- Model monitoring dashboard
- Data drift monitoring using Population Stability Index (PSI)
- Fairness monitoring
- Human-reviewed retraining triggers
- Prediction explanation audit records
- Automated testing with Pytest
- Continuous Integration using GitHub Actions
- Docker and Docker Compose configuration
- Responsible AI governance documentation

## Repository Structure

- `data/` – project datasets and processed data
- `notebooks/` – analysis and model development notebooks
- `pipeline/` – data pipeline and governance components
- `src/` – supporting project source code
- `tests/` – automated pipeline and monitoring tests
- `monitoring/` – drift, fairness, retraining, explanation, and monitoring components
- `dashboard/` – dashboard-related project files
- `models/` – model-related files
- `docs/` – responsible AI and governance documentation
- `reports/` – project reports
- `.github/workflows/` – Continuous Integration workflow
- `Dockerfile` – reproducible container configuration
- `docker-compose.yml` – configuration for project services

## Responsible AI

The prototype follows a human-in-the-loop approach. Model predictions are intended to support decision-making and must not be used independently to deny healthcare, automatically cancel appointments, or restrict patient access to care.

Monitoring controls are included for model performance, data drift, fairness, and responsible AI risks. Significant alerts are designed to trigger human review rather than automatic model retraining or deployment.

## Monitoring and Governance

The repository includes:

- A Model Monitoring Policy
- An Algorithmic Impact Assessment
- An AI Incident Response Plan
- Data drift monitoring
- Fairness monitoring
- Retraining review triggers
- Explanation audit storage

These components support transparency, accountability, and continuous review of the prototype.

## Testing and Continuous Integration

Automated tests are implemented using Pytest. GitHub Actions runs the test suite when changes are pushed to the repository, helping verify that pipeline and monitoring components continue to function as expected.

## Project Status

Academic prototype developed for the BAN6800 Capstone Project.

The system demonstrates an end-to-end analytics workflow from data preparation and modelling through visualization, monitoring, testing, and responsible AI governance.

## Prediction API

A FastAPI prediction endpoint is included to demonstrate how the trained Random Forest model can be accessed programmatically.

### Run the API

From the `BAN6800_Module_4_Trinitas_Iwunze` directory:

```bash
python -m uvicorn app:app --host 127.0.0.1 --port 8000
```

Interactive API documentation is available at /docs.

The /predict endpoint accepts appointment characteristics and returns:
- Predicted class
- Predicted outcome (No-show or Show)
- No-show probability
- A responsible-use notice
The API is intended for planning and reminder-support purposes only. Predictions must not be used to automatically cancel appointments, deny care, or restrict patient access.
### Model Compatibility
The serialized Random Forest model requires scikit-learn==1.6.1, which is pinned in requirements.txt for reproducibility.
