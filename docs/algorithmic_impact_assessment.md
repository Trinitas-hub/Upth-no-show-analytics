# Algorithmic Impact Assessment (AIA)

## UPTH Outpatient Appointment No-Show Prediction Prototype

**Project:** UPTH No-Show Analytics  
**Institutional Context:** University of Port Harcourt Teaching Hospital (UPTH), Rivers State, Nigeria  
**Project Type:** Academic healthcare analytics prototype  
**Assessment Purpose:** Responsible AI governance and risk assessment  

## 1. Purpose and Intended Use

The UPTH No-Show Analytics project is an academic prototype designed to predict the risk of outpatient appointment non-attendance. Its purpose is to demonstrate how predictive analytics could support hospital staff in identifying appointments that may benefit from additional reminders or administrative follow-up.

The model is intended to support human decision-making rather than replace it. A patient's predicted no-show risk must not be used to automatically cancel an appointment, deny healthcare, reduce access to treatment, or penalize a patient.

The prototype was developed using the publicly available Medical Appointment No Shows dataset as a proxy dataset. It does not represent a live UPTH production system.

## 2. Stakeholders

The main stakeholders potentially affected by the system include:

- Patients attending outpatient services
- Clinicians and other healthcare professionals
- Appointment and administrative staff
- Hospital management
- ICT and data analytics personnel
- Data protection and governance personnel

Patients are the most important affected group because inappropriate use of predictions could influence access to healthcare services.

## 3. Potential Benefits

Potential benefits of a responsibly implemented no-show prediction system include:

- Earlier identification of appointments at higher risk of non-attendance
- Better targeting of appointment reminders and follow-up
- Improved use of outpatient appointment capacity
- Reduced administrative disruption caused by missed appointments
- Better evidence to support operational planning

These benefits are potential outcomes and have not been demonstrated in a live UPTH deployment.

## 4. Potential Risks and Harms

The project presents several important risks.

### Bias and Discrimination

Prediction errors may not be distributed equally across demographic groups. If predictions are used without fairness monitoring, particular groups could receive disproportionate interventions.

### Patient Access

A high-risk prediction could be misinterpreted as evidence that a patient does not value healthcare. The model must therefore never be used as the sole basis for cancelling appointments or restricting access to care.

### Privacy and Confidentiality

Healthcare information is sensitive. Production implementation would require appropriate access controls, data minimization, secure storage, anonymization or pseudonymization where appropriate, and compliance with applicable data-protection requirements.

### Model Drift

Patient behaviour and healthcare processes may change over time. A model that initially performs adequately may become less reliable if the characteristics of future data differ from its development data.

### Automation Bias

Staff may place excessive confidence in a model prediction. Predictions must therefore be presented as decision-support information rather than unquestionable conclusions.

## 5. Fairness and Equity Controls

The prototype incorporates fairness assessment and monitoring principles.

Fairness monitoring includes comparison of prediction selection rates between demographic groups, demographic parity difference, and disparate impact ratio.

For the monitoring prototype:

- Demographic parity difference above 0.10 triggers review.
- Disparate impact ratio below 0.80 triggers review.

These values are monitoring triggers rather than automatic declarations that a model is fair or unfair.

Any significant disparity should be investigated before decisions are made about continued model use or retraining.

## 6. Explainability and Transparency

Model explainability is supported through feature-level explanations, including the project's SHAP-based analysis.

An Explanation Store prototype has also been included to demonstrate how prediction-level explanations could be retained for authorized audit and review.

Explanation records should not contain directly identifying patient information.

## 7. Monitoring and Model Drift

The monitoring framework uses Population Stability Index (PSI) to identify changes between reference and current feature distributions.

The prototype uses the following monitoring thresholds:

- PSI below 0.10: no significant drift
- PSI from 0.10 to 0.25: investigate moderate drift
- PSI above 0.25: significant drift requiring model review

Monitoring should also include model performance and fairness indicators.

A decline in recall of more than 0.05 from the validated baseline is used in the prototype as a performance-review trigger.

## 8. Human Oversight and Retraining

The project does not permit uncontrolled automatic retraining and deployment.

When monitoring thresholds are exceeded, the system generates a human-review trigger. Authorized stakeholders should investigate data quality, model performance, fairness, and operational circumstances before deciding whether retraining is appropriate.

A newly trained model should be validated before replacing an existing approved model.

## 9. Privacy and Data Governance

The project follows the principles of:

- Data minimization
- Purpose limitation
- Controlled access
- Confidentiality
- Traceability
- Secure handling of sensitive information

The academic prototype uses a public proxy dataset rather than live UPTH patient records.

Any future implementation using real hospital data would require formal institutional authorization, appropriate security controls, and compliance with applicable Nigerian data-protection requirements.

## 10. Accountability

Responsibility for the system should remain with human stakeholders.

A production governance structure should include appropriate representation from:

- Clinical services
- Hospital administration
- ICT/data teams
- Data protection or privacy functions
- Model governance or analytics personnel

Significant incidents, fairness concerns, performance degradation, and proposed model changes should be documented and reviewed.

## 11. Overall Impact Classification

**Impact Level: High**

The prototype is classified as potentially high impact because its intended context is healthcare and its predictions could affect how patients are treated operationally if improperly used.

The high-impact classification does not mean the prototype itself makes clinical decisions. Instead, it indicates that strong governance, monitoring, transparency, privacy protection, and human oversight would be required before real-world implementation.

## 12. Decision and Safeguards

The prototype may be used for academic demonstration and further controlled evaluation.

It should not be treated as a clinically deployed UPTH system.

Before any real-world implementation, the system would require institutional approval, validation using appropriate local data, privacy and security review, fairness evaluation, operational testing, and defined human oversight procedures.

The central safeguard remains:

**No patient should be denied healthcare or have an appointment automatically cancelled solely because of a predicted no-show risk.**
