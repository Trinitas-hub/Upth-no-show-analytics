# Model Monitoring Policy

## UPTH Outpatient Appointment No-Show Prediction Prototype

**Project:** UPTH No-Show Analytics  
**Institutional Context:** University of Port Harcourt Teaching Hospital (UPTH), Rivers State, Nigeria  
**Project Type:** Academic healthcare analytics prototype  
**Purpose:** Define how model performance, data drift, fairness, and responsible AI risks will be monitored over time.

## 1. Purpose

This Model Monitoring Policy describes how the UPTH outpatient appointment no-show prediction prototype should be monitored after deployment.

The purpose of monitoring is to identify changes in model performance, input data, fairness, or system behavior that could reduce the reliability or responsible use of the model.

The current project is an academic prototype developed using the publicly available Medical Appointment No Shows dataset as a proxy dataset. It does not represent a live UPTH production system.

## 2. Monitoring Principles

The monitoring process is based on the following principles:

- Model predictions should support human decision-making rather than replace it.
- Monitoring should identify potential problems before they significantly affect users.
- Model performance should be reviewed regularly.
- Changes in incoming data should be checked for data drift.
- Fairness should be monitored across relevant demographic groups.
- Significant monitoring alerts should trigger human review.
- Retraining and redeployment must not occur automatically without appropriate review and validation.

## 3. Model Performance Monitoring

The model should be monitored using appropriate classification metrics, including:

- ROC-AUC
- Precision
-  Recall
- F1-score

Particular attention should be given to **recall**, because missed identification of patients who may not attend could reduce the usefulness of the prediction system.

Current model performance should be compared with the validated baseline model performance. Significant deterioration should trigger investigation and human review.
## 4. Data Drift Monitoring

Changes in the characteristics of incoming data should be monitored because significant changes may affect model reliability.

Population Stability Index (PSI) will be used as a simple method for identifying changes between reference data and current data.

The following thresholds will be used:

- PSI < 0.10: No significant drift.
- PSI from 0.10 to 0.25: Moderate drift requiring review.
- PSI > 0.25: Significant drift requiring investigation.

A significant drift alert should trigger human review to determine whether changes in the data are temporary, expected, or likely to affect model performance.

## 5. Fairness Monitoring

Model predictions should be monitored for potential differences across relevant demographic groups.

The monitoring prototype includes:

- Selection rate.
- Demographic parity difference.
- Disparate impact ratio.

Fairness metrics should be interpreted carefully and should not be used alone to determine whether the model is fair or unfair.

A demographic parity difference greater than 0.10 or a disparate impact ratio below 0.80 should trigger further human review.

## 6. Retraining Triggers

Model retraining should be considered when monitoring identifies significant changes that may affect model reliability or fairness.

Potential triggers include:

- PSI greater than 0.25.
- Demographic parity difference greater than 0.10.
- Disparate impact ratio below 0.80.
- Meaningful deterioration in model recall compared with the validated baseline.
- Repeated monitoring alerts or significant changes in the underlying data.

A trigger does not automatically retrain the model. It initiates a human review to determine whether retraining is necessary.
## 7. Monitoring Frequency

For a future production implementation, monitoring should occur on a regular schedule.

- Model performance should be reviewed periodically when new outcome data become available.
- Data drift should be assessed whenever a meaningful batch of new data is received.
- Fairness metrics should be reviewed alongside model performance.
- Significant alerts should be investigated as soon as reasonably possible.
- A full monitoring review should also occur before any model retraining or redeployment.

The exact monitoring frequency should be determined by UPTH based on data volume, clinical workflow, operational requirements, and governance policies.

## 8. Human Oversight and Escalation

Monitoring alerts are indicators for investigation and must not be treated as automatic decisions.

When a threshold is exceeded, authorized personnel should review the monitoring results, investigate the cause, assess potential patient impact, and determine the appropriate response.

Where a serious performance, fairness, privacy, or security concern is identified, the issue should be handled according to the project's AI Incident Response Plan.

## 9. Monitoring Records

Monitoring activities should be documented to support transparency and accountability.

Records should include:

- Date of monitoring review.
- Model version.
- Performance metrics.
- Data drift results.
- Fairness metrics.
- Alerts or thresholds exceeded.
- Investigation findings.
- Actions taken.
- Reviewer or responsible team.

## 10. Review and Continuous Improvement

This Model Monitoring Policy should be reviewed when significant changes are made to the model, dataset, monitoring thresholds, deployment environment, or governance requirements.

Monitoring results and lessons learned should be used to improve model validation, responsible AI controls, documentation, and future model development.
