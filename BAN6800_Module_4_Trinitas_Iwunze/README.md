# BAN6800 Module 4 – Predictive Model Development & Validation

## UPTH Outpatient Appointment No-Show Prediction

**Student:** Trinitas Chideziri Iwunze  
**Course:** BAN6800 Capstone  
**University:** Nexford University  
**Module:** Module 4 – Predictive Model Development & Validation Pack  

## Project Overview

This repository contains the technical deliverables for Module 4 of my BAN6800 Capstone project. The project focuses on developing, validating, explaining, and assessing the fairness of a machine learning model for predicting outpatient appointment no-shows.

The analysis builds on the cleaned and validated dataset prepared in Module 3. The final dataset contains 110,521 appointment records, with 79.81% attended appointments and 20.19% no-shows.

The model is intended as a decision-support prototype for appointment planning, reminders, and administrative follow-up. It is not intended to automatically cancel appointments, deny healthcare, or replace human judgement.

## Model Development

I evaluated the following approaches:

- Majority-class baseline
- Logistic Regression
- Balanced Logistic Regression
- Random Forest
- Tuned Random Forest

An 80/20 stratified train/test split was used, resulting in 88,416 training records and 22,105 testing records.

The tuned Random Forest was selected as the main candidate model. It used 150 trees, a maximum depth of 20, and balanced class weights.

### Final Model Performance

| Metric | Result |
|---|---:|
| Accuracy | 0.6575 |
| Precision | 0.3321 |
| Recall | 0.6892 |
| F1-score | 0.4483 |
| ROC-AUC | 0.7383 |

## Explainability and Fairness

SHAP was used for global and local model explanations. AppointmentLeadTime and Age were among the most influential features.

Fairness was assessed across gender and age groups using demographic parity, disparate impact, true positive rates, false positive rates, and predicted no-show rates.

A bias-mitigation experiment was also conducted by removing Age and retraining the Random Forest. The experiment showed that removing a protected attribute alone did not eliminate demographic differences.

Sensitivity and counterfactual analysis was performed using AppointmentLeadTime to examine how changes in this feature affected an individual prediction.

## MLflow Experiment Tracking

MLflow was used to record the selected model's parameters and evaluation metrics.

The final model was registered as:

`UPTH_No_Show_Random_Forest`

**Version:** 1

Evidence from the MLflow experiment and Model Registry is available in the `MLflow_Evidence` folder.

## Repository Contents

| File/Folder | Description |
|---|---|
| `Module4_Model_Development.ipynb` | Model development, validation, SHAP, fairness, mitigation, and sensitivity analysis |
| `Model_Validation_Report BAN 6800.docx` | Main Module 4 Model Validation Report |
| `Fairness Metrics Report.docx` | Detailed fairness assessment |
| `Model Card.docx` | Model performance, intended use, fairness, limitations, risks, and monitoring |
| `MLflow_Evidence/` | Screenshots of MLflow experiment tracking and Model Registry |
| `upth_no_show_random_forest.joblib` | Serialized tuned Random Forest model |
| `app.py` | FastAPI application containing the `/predict` endpoint |

## API Prototype

The `app.py` file provides a FastAPI prototype that loads the serialized Random Forest model and exposes a `/predict` endpoint.

The endpoint returns the predicted appointment outcome and estimated no-show probability.

## Responsible Use

The model should only support low-risk interventions such as appointment reminders and administrative follow-up.

Predictions must not be used to automatically cancel appointments or deny patients access to healthcare. Human oversight remains necessary.

The dataset used for this prototype may differ from the actual UPTH patient population. Therefore, local validation, continued fairness assessment, and performance monitoring would be required before real-world deployment.

## Conclusion

Module 4 demonstrates the development of a predictive model together with model validation, explainability, fairness assessment, bias mitigation, sensitivity analysis, experiment tracking, model serialization, and an API prototype.

The tuned Random Forest achieved a ROC-AUC of 0.7383 and a no-show recall of 0.6892. The results demonstrate the importance of considering predictive performance alongside explainability, fairness, responsible use, and human oversight.
