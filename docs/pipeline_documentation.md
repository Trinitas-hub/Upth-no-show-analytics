# UPTH No-Show Analytics Pipeline Documentation

## Project Overview

This data pipeline supports my capstone project on predicting outpatient appointment no-shows at the University of Port Harcourt Teaching Hospital (UPTH).

The Medical Appointment No Shows dataset is used as a public proxy dataset for developing and demonstrating the analytics workflow. It does not contain actual UPTH patient records, so the results should not be interpreted as findings about UPTH patients.

The purpose of the pipeline is to transform raw appointment data into a clean, validated, privacy-prepared dataset that can support predictive modeling in Module 4.

## Pipeline Workflow

The implemented workflow follows these stages:

**Raw Appointment Data → Data Ingestion → Cleaning → Transformation → Validation → Privacy Preparation → Model-Ready Data**

Prefect is used to organize the main data-processing tasks into a reproducible workflow.

## 1. Data Source and Ingestion

The pipeline uses the Medical Appointment No Shows CSV dataset.

- Raw records: 110,527
- Source format: CSV
- Input file: `data/KaggleV2-May-2016.csv`

The Prefect ingestion task loads the appointment records into a Pandas DataFrame for processing.

## 2. Data Cleaning

The cleaning stage checks the dataset for data-quality problems, including:

- Duplicate records
- Missing target values
- Invalid age values
- Invalid or inconsistent records

During data-quality assessment, one record with an age of -1 was identified as invalid.

The cleaning and subsequent transformation rules reduced the dataset from 110,527 raw records to 110,521 model-ready records.

## 3. Data Transformation

The transformation stage prepares variables for future predictive modeling.

An appointment lead-time feature is derived from the difference between `AppointmentDay` and `ScheduledDay`.

The `No-show` outcome is also transformed into a binary model target for future machine-learning development.

Records that do not satisfy the defined transformation and quality rules are excluded from the final processed dataset.

## 4. Data Validation

Great Expectations is used to apply structured data-quality checks.

The validation checks include:

- Missing values in key fields
- Valid age range
- Expected no-show categories
- Expected gender categories
- Required appointment-date fields

Initial validation of the raw data identified a quality issue. After cleaning and transformation, Great Expectations was rerun on the processed dataset.

**Final validation result: DATA QUALITY GATE PASSED**

Only data that satisfies the defined validation requirements is allowed to proceed as model-ready data.

## 5. Unit Testing

Pytest is used to test important pipeline functions.

Four unit tests were implemented to verify:

1. Removal of invalid age values
2. Removal of duplicate records
3. Creation of appointment lead time
4. Creation of the binary no-show target

**Test result: 4 tests passed**

## 6. Demographic Representation Assessment

Demographic representation and observed no-show patterns were assessed across gender and age groups.

The processed dataset contained approximately:

- Female: 65.0% of appointment records
- Male: 35.0% of appointment records

Observed no-show rates were approximately 20.3% for females and 20.0% for males.

Across age groups, the highest observed no-show rate was approximately 24.0% among patients aged 18–34, while the 65+ group had an observed rate of approximately 15.5%.

These results are descriptive checks of representation and outcome patterns and do not establish model bias. Model-level fairness assessment will be conducted when predictive models are developed and evaluated.

## 7. Privacy Preparation

A privacy-preparation script removes direct identifiers before analytical use.

The following identifier columns were removed:

- `PatientId`
- `AppointmentID`

The resulting privacy-prepared dataset retained 110,521 appointment records.

Removal of these direct identifiers is treated as a data-minimization measure and does not imply that the remaining dataset is completely anonymous.

## 8. Privacy Audit Logging

A privacy audit script records privacy-related processing activities.

The audit log captures:

- UTC timestamp
- Action performed
- Dataset involved
- Description of the activity

Recorded activities include dataset access, removal of direct identifiers, creation of the privacy-prepared output, and documented access restrictions.

## 9. Governance and Human Oversight

The project applies principles of:

- Data minimization
- Purpose limitation
- Restricted access
- Data quality
- Accountability
- Fairness
- Human oversight

Analytics outputs are intended to support healthcare staff and should not be used to automatically cancel appointments, deny healthcare services, or disadvantage patients.

The governance approach is designed to align with the Nigeria Data Protection Act 2023 and the Ethical AI principles established earlier in the capstone.

## 10. Reproducibility

The project repository contains:

- Prefect pipeline
- Great Expectations validation script
- Pytest unit tests
- Dockerfile
- Requirements file
- Demographic assessment script
- Data anonymization script
- Privacy audit script
- Data governance documentation

A Dockerfile has been created to define a consistent Python environment for the project. The Docker container should be built and tested before claiming successful container execution.

## 11. Output and Module 4 Transition

The final processed dataset is stored as:

`data/processed_appointments.csv`

The privacy-prepared output is stored as:

`data/anonymized_appointments.csv`

The validated and prepared data provides the foundation for the next stage of the capstone, where predictive models will be developed and evaluated in Module 4.
