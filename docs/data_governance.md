# Data Governance Framework

## UPTH Outpatient Appointment No-Show Analytics Project

### Purpose
This governance framework defines how data used in the UPTH outpatient appointment no-show analytics project will be handled responsibly throughout the data pipeline. It builds on the privacy, fairness, accountability, and human-oversight principles established in Modules 1 and 2.

### Data Access
Access to appointment data and analytical outputs should be limited to authorized personnel involved in the project. Access should follow the principle of least privilege so that users only have access to the information required for their responsibilities.

### Privacy and Data Minimization
Only data required for the stated analytical purpose should be retained. Direct identifiers such as PatientId and AppointmentID are removed from the analytical dataset before further use. Remaining variables should continue to be treated as potentially sensitive and handled securely.

### Data Quality
Data quality checks are applied before data proceeds to predictive modeling. Missing values, duplicates, invalid age values, date inconsistencies, data types, and categorical values are assessed during pipeline processing and validation.

### Fairness and Bias
Demographic representation and outcome patterns are reviewed across relevant groups, including gender and age groups. These checks are used to identify areas requiring further investigation. Model-level fairness assessment will be required when predictive models are developed and evaluated.

### Human Oversight
Analytics outputs are intended to support healthcare staff rather than replace professional judgment. Predicted no-show risk should not be used to automatically cancel appointments, deny healthcare services, or disadvantage patients.

### Audit and Accountability
Privacy-related processing activities are recorded in an audit log, including dataset access, identifier removal, creation of privacy-prepared outputs, and documented access restrictions. This supports traceability and accountability.

### Data Retention
Project data should be retained only for as long as required for the approved analytical purpose. Unnecessary copies and temporary files should be securely removed when they are no longer required.

### Legal and Ethical Alignment
The project is designed to support responsible data processing principles consistent with the Nigeria Data Protection Act 2023, including purpose limitation, data minimization, security, transparency, and accountability.

### Dataset Limitation
The Medical Appointment No Shows dataset is a public proxy dataset and does not contain actual UPTH patient records. Therefore, findings from this project should not be presented as evidence about UPTH patients. Any future implementation at UPTH would require authorized, appropriately protected, and locally representative data.
