# AI Incident Response Plan

## UPTH Outpatient Appointment No-Show Prediction Prototype

**Project:** UPTH No-Show Analytics  
**Institutional Context:** University of Port Harcourt Teaching Hospital (UPTH), Rivers State, Nigeria  
**System Type:** Academic healthcare analytics prototype  
**Purpose:** Define how potential AI-related incidents should be identified, reported, investigated, contained, resolved, and documented.

## 1. Purpose

This Incident Response Plan establishes a structured process for responding to problems that may arise from the UPTH outpatient appointment no-show prediction prototype.

The objective is to protect patients, maintain responsible human oversight, preserve data integrity, and ensure that model-related concerns are investigated before the system continues to be used.

The current project is an academic prototype based on a public proxy dataset. It is not a live UPTH production system.

## 2. What Constitutes an AI Incident?

An AI incident is any event that may affect the reliability, fairness, privacy, security, or appropriate use of the prediction system.
Examples include:

- A significant drop in model performance.
- Unexpected changes in incoming data or data drift.
- Evidence that predictions may disadvantage a demographic group.
- Incorrect or misleading prediction explanations.
- Unauthorized access to prediction data or audit records.
- Use of predictions to automatically deny, cancel, or restrict patient care.
- Failure of the monitoring or prediction service.

## 3. Incident Severity Levels

Incidents should be classified according to their potential impact.

### Low Severity

Minor technical or monitoring issues that do not affect patient access, privacy, or model reliability.

### Medium Severity

Issues such as moderate data drift, unexpected changes in model performance, or fairness concerns that require investigation.

### High Severity

Serious incidents involving patient safety, significant unfairness, privacy breaches, unauthorized access, or inappropriate automated healthcare decisions.
## 4. Incident Response Process

When an AI-related incident is identified, the following process should be followed:

1. **Identify and Report**  
   The incident should be documented and reported to the appropriate project or oversight personnel.

2. **Assess**  
   Determine the severity of the incident and identify whether model performance, fairness, privacy, security, or patient access may be affected.

3. **Contain**  
   If necessary, suspend the affected model or monitoring component until the issue has been investigated.

4. **Investigate**  
   Review model outputs, monitoring results, audit logs, data quality checks, and relevant documentation to determine the cause.

5. **Resolve**  
   Correct the identified issue. This may include fixing data problems, adjusting monitoring controls, reviewing the model, or initiating retraining.

6. **Validate Before Reuse**  
   Any updated model or component must be tested and reviewed before it is returned to use.

7. **Document and Close**  
   Record the incident, actions taken, outcome, and any lessons learned.

## 5. Human Oversight

All significant incidents require human review. Automated monitoring may identify potential problems, but it must not independently retrain, redeploy, or make healthcare access decisions.

The final decision to modify, retrain, approve, or withdraw a model must remain with authorized human personnel.
## 6. Roles and Responsibilities

- **Clinical Staff:** Report concerns relating to patient care or inappropriate use of model predictions.
- **Data/Analytics Team:** Investigate model performance, data drift, fairness, and technical issues.
- **ICT Personnel:** Address system availability, access control, and security incidents.
- **Data Protection/Governance Personnel:** Review privacy, data protection, and compliance concerns.
- **Hospital Management:** Provide oversight and approve significant corrective actions.

## 7. Incident Documentation

Each incident record should include:

- Date and time of the incident.
- Description of the issue.
- Severity classification.
- Systems, data, or stakeholders affected.
- Investigation findings.
- Corrective actions taken.
- Person or team responsible.
- Validation performed before returning the system to use.
- Final resolution and lessons learned.

## 8. Responsible AI Safeguard

The UPTH no-show prediction prototype is intended only to support human decision-making. A prediction must never be used by itself to deny healthcare, automatically cancel an appointment, or restrict a patient's access to treatment.

Any model performance, fairness, privacy, or security concern that could affect patients should trigger human review before further action is taken.

## 9. Review and Continuous Improvement

This Incident Response Plan should be reviewed whenever significant changes are made to the model, data pipeline, monitoring process, or governance requirements.

Lessons learned from incidents should be used to improve monitoring, documentation, testing, and responsible AI controls.
