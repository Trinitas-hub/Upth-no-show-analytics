import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="UPTH Model Monitoring",
    page_icon="📊",
    layout="wide"
)

st.title("UPTH No-Show Prediction Model Monitoring")
st.caption(
    "Monitoring prototype for model performance, data drift, "
    "fairness, and responsible AI oversight."
)

st.info(
    "This dashboard is a monitoring prototype based on the "
    "Medical Appointment No Shows proxy dataset. It does not "
    "represent a live UPTH production system."
)

# ---------------------------------------------------------
# BASELINE MODEL PERFORMANCE
# ---------------------------------------------------------

st.header("1. Baseline Model Performance")

st.write(
    "The values below represent the validated baseline performance "
    "of the selected tuned Random Forest model."
)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Accuracy", "65.75%")
col2.metric("Precision", "33.21%")
col3.metric("Recall", "68.92%")
col4.metric("F1 Score", "44.83%")
col5.metric("ROC-AUC", "73.83%")

st.warning(
    "Precision is relatively low. Predictions should therefore be "
    "used for supportive interventions such as reminders and follow-up, "
    "not automatic appointment cancellation or denial of care."
)

# ---------------------------------------------------------
# DATA DRIFT MONITORING
# ---------------------------------------------------------

st.header("2. Data Drift Monitoring")

st.write(
    "Population Stability Index (PSI) can be used to compare incoming "
    "data with the model's reference data."
)

psi_thresholds = pd.DataFrame({
    "PSI Range": ["< 0.10", "0.10 – 0.25", "> 0.25"],
    "Interpretation": [
        "No significant drift",
        "Moderate drift – investigate",
        "Significant drift – review model"
    ]
})

st.dataframe(psi_thresholds, use_container_width=True)

st.info(
    "No live production data are currently connected. Therefore, "
    "this section defines the monitoring thresholds rather than "
    "claiming that production drift has been observed."
)

# ---------------------------------------------------------
# FAIRNESS MONITORING
# ---------------------------------------------------------

st.header("3. Fairness Monitoring")

st.write(
    "Fairness should be reviewed across demographic groups, particularly "
    "gender and age groups, because the validation stage identified "
    "larger disparities across age groups."
)

fairness_data = pd.DataFrame({
    "Indicator": [
        "Gender demographic parity difference",
        "Gender disparate impact",
        "Age-group disparity"
    ],
    "Baseline finding": [
        "0.0483",
        "0.8892",
        "Requires continued monitoring"
    ]
})

st.dataframe(fairness_data, use_container_width=True)

st.warning(
    "A fairness alert should trigger human review when material disparities "
    "emerge or existing disparities worsen. Model predictions must not be "
    "used automatically to restrict access to healthcare."
)

# ---------------------------------------------------------
# MONITORING ACTIONS
# ---------------------------------------------------------

st.header("4. Monitoring and Response Actions")

st.markdown(
    """
    - Review model performance when new labelled outcomes become available.
    - Investigate moderate or significant data drift.
    - Compare fairness metrics across demographic groups.
    - Document monitoring findings and corrective actions.
    - Retrain only after data quality, performance, and fairness review.
    - Require human approval before deploying an updated model.
    """
)

st.success(
    "Monitoring framework configured for responsible model oversight."
)
