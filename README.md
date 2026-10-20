# UPTH No-Show Analytics

## Project Overview

UPTH No-Show Analytics is an academic healthcare analytics prototype developed for the BAN6800 Capstone Project. It explores the prediction of outpatient appointment no-shows in the context of the University of Port Harcourt Teaching Hospital (UPTH), Rivers State, Nigeria.

The project uses the publicly available Medical Appointment No Shows dataset as a proxy dataset. Therefore, the results do not represent actual UPTH patient outcomes or a live UPTH production system.

The objective is to demonstrate how machine learning, data validation, explainable AI, fairness assessment, monitoring, and visualization can support healthcare decision-making while maintaining human oversight.

## Project Links

### GitHub Repository
https://github.com/Trinitas-hub/Upth-no-show-analytics

### Stakeholder, Explainability and Monitoring Dashboard
https://upth-no-show-analytics.streamlit.app/

### Live Prediction API
https://upth-no-show-analytics.onrender.com/predict

### Interactive API Documentation
https://upth-no-show-analytics.onrender.com/docs

## Project Components

The repository includes:

- Data preprocessing and validation
- Feature engineering
- Logistic Regression and Random Forest modelling
- Model performance evaluation
- MLflow experiment tracking and Model Registry
- SHAP model explainability
- Fairness assessment
- Streamlit stakeholder dashboard
- Model performance monitoring
- Data drift monitoring using Population Stability Index (PSI)
- Fairness monitoring
- Human-reviewed retraining triggers
- Prediction explanation audit records
- FastAPI prediction service
- Automated testing with Pytest
- Continuous Integration using GitHub Actions
- Docker and Docker Compose configuration
- Responsible AI and governance documentation

## Repository Structure

- `data/` – raw and processed project datasets
- `notebooks/` – data analysis and model development notebooks
- `pipeline/` – data pipeline and governance components
- `src/` – supporting project source code
- `tests/` – automated pipeline and monitoring tests
- `monitoring/` – drift, fairness, retraining, explanation, and monitoring components
- `dashboard/` – dashboard-related project files
- `models/` – trained model-related files
- `docs/` – responsible AI and governance documentation
- `reports/` – project reports
- `.github/workflows/` – GitHub Actions CI workflow
- `Dockerfile` – reproducible container configuration
- `docker-compose.yml` – multi-service project configuration
- `requirements.txt` – required Python dependencies

## Setup

Clone or download the repository and install the required dependencies:

pip install -r requirements.txt

The project uses Python and the dependencies specified in `requirements.txt`.

## Prediction API

A FastAPI prediction endpoint is included to demonstrate how the trained Random Forest model can be accessed programmatically.

### Run the API Locally

From the `BAN6800_Module_4_Trinitas_Iwunze` directory:

python -m uvicorn app:app --host 127.0.0.1 --port 8000

Interactive API documentation is available at `/docs`.

The `/predict` endpoint accepts appointment characteristics and returns:

- Predicted class
- Predicted outcome (No-show or Show)
- No-show probability
- Responsible-use notice

The API is intended for planning, reminder, and follow-up support only. Predictions must not be used to automatically cancel appointments, deny healthcare, or restrict patient access.

## Model Explainability

SHAP is used to explain the factors influencing model predictions. The project includes both global and individual prediction explanations to make model behaviour more understandable to stakeholders.

Explainability information is incorporated into the Streamlit dashboard.

## Fairness Monitoring

Fairness assessment is included to examine differences in model behaviour across demographic groups. Fairness indicators are monitored as part of the responsible AI framework.

Fairness alerts are intended to trigger human investigation and review rather than automatic changes to the model.

## Monitoring and Retraining

The project includes monitoring for:

- Model performance
- Data drift
- Fairness
- Responsible AI risks
- Prediction explanations

Population Stability Index (PSI) thresholds are used to identify potential data drift.

Retraining triggers are defined to support human review when significant performance, drift, or fairness concerns are detected. Automated retraining and deployment are not performed without human review in this academic prototype.

## Testing and Continuous Integration

Automated tests are implemented using Pytest. GitHub Actions provides the project's CI workflow and runs automated checks when changes are pushed to the repository.

This helps verify that pipeline, monitoring, and related project components continue to function as expected.

## Docker and Docker Compose

The repository includes a `Dockerfile` and `docker-compose.yml` to support a reproducible containerized environment and organize project services.

## Responsible AI and Governance

The project follows a human-in-the-loop approach. Model predictions are intended to support healthcare professionals rather than replace professional judgment.

A patient identified as having a higher predicted no-show risk may receive supportive interventions, such as an additional reminder or administrative follow-up. Predictions must not be used independently to deny healthcare, automatically cancel appointments, or restrict access to care.

The repository includes:

- Model Monitoring Policy
- Algorithmic Impact Assessment
- AI Incident Response Plan
- Data drift monitoring
- Fairness monitoring
- Retraining review triggers
- Explanation audit storage

These components support transparency, fairness, accountability, privacy, and continuous review of the prototype.

## Model Compatibility

The serialized Random Forest model requires:

scikit-learn==1.6.1

This version is pinned in `requirements.txt` to support reproducibility.

## Project Status

This project is an academic prototype developed for the BAN6800 Capstone Project.

It demonstrates an end-to-end analytics workflow covering data preparation, validation, predictive modelling, model evaluation, explainability, fairness assessment, API deployment, stakeholder visualization, monitoring, automated testing, CI, containerization, and responsible AI governance.

The system is not a live UPTH clinical system and would require validation using authorized local UPTH data before any real-world healthcare implementation.
