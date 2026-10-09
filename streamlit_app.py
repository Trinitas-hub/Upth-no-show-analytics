
import streamlit as st
import pandas as pd

# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------
st.set_page_config(
    page_title="UPTH No-Show Analytics",
    page_icon="🏥",
    layout="wide"
)

# --------------------------------------------------
# TITLE
# --------------------------------------------------
st.title("🏥 UPTH Outpatient No-Show Analytics")

st.write(
    "An interactive decision-support dashboard for understanding "
    "outpatient appointment no-show risk."
)

st.info(
    "This prototype is intended to support human decision-making. "
    "Predicted risk should not be used to automatically cancel appointments "
    "or deny patients access to healthcare."
)

# --------------------------------------------------
# PROJECT OVERVIEW
# --------------------------------------------------
st.header("Project Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Validated Appointments",
        value="110,521"
    )

with col2:
    st.metric(
        label="No-Show Appointments",
        value="22,314"
    )

with col3:
    st.metric(
        label="No-Show Rate",
        value="20.19%"
    )

st.divider()

# --------------------------------------------------
# MODEL PERFORMANCE
# --------------------------------------------------
st.header("Model Performance")

m1, m2, m3, m4, m5 = st.columns(5)

with m1:
    st.metric("Accuracy", "65.75%")

with m2:
    st.metric("Precision", "33.21%")

with m3:
    st.metric("Recall", "68.92%")

with m4:
    st.metric("F1 Score", "44.83%")

with m5:
    st.metric("ROC-AUC", "73.83%")

st.write(
    "The tuned Random Forest identifies many actual no-shows, reflected "
    "in its 68.92% recall. However, the lower precision of 33.21% means "
    "that some patients who would attend may also be flagged as possible "
    "no-shows."
)

st.divider()

# --------------------------------------------------
# EXAMPLE PREDICTIONS
# --------------------------------------------------
st.header("Understanding Individual Predictions")

st.write(
    "The following examples demonstrate how predicted no-show risk "
    "can vary across individual appointments."
)

example1, example2, example3 = st.columns(3)

with example1:
    st.subheader("Example 1 — Borderline Case")
    st.write("**Actual Outcome:** No-Show")
    st.write("**Predicted Outcome:** Attend")
    st.metric(
        "No-Show Probability",
        "48.53%"
    )
    st.write(
        "The probability was just below the 50% classification threshold. "
        "The model therefore predicted Attend, although the patient "
        "actually missed the appointment."
    )

with example2:
    st.subheader("Example 2 — Lower-Risk Case")
    st.write("**Actual Outcome:** Attend")
    st.write("**Predicted Outcome:** Attend")
    st.metric(
        "No-Show Probability",
        "11.53%"
    )
    st.write(
        "The model estimated a low no-show risk and correctly classified "
        "this appointment as Attend."
    )

with example3:
    st.subheader("Example 3 — Higher-Risk Case")
    st.write("**Actual Outcome:** No-Show")
    st.write("**Predicted Outcome:** No-Show")
    st.metric(
        "No-Show Probability",
        "71.48%"
    )
    st.write(
        "The model estimated a higher no-show risk and correctly classified "
        "this appointment as No-Show."
    )

st.warning(
    "Predicted probabilities represent estimated risk, not certainty. "
    "Individual predictions should support, rather than replace, "
    "staff judgement."
)

st.divider()

# --------------------------------------------------
# WHAT-IF ANALYSIS
# --------------------------------------------------
st.header("What-If Analysis: Appointment Lead Time")

w1, w2, w3 = st.columns(3)

with w1:
    st.metric(
        "0-Day Lead Time",
        "26.62%"
    )

with w2:
    st.metric(
        "30-Day Lead Time",
        "54.08%"
    )

with w3:
    st.metric(
        "Classification Threshold",
        "50%"
    )

st.write(
    "For the selected appointment, the predicted no-show probability "
    "crossed the 50% classification threshold between the tested "
    "3-day and 7-day lead times."
)

st.caption(
    "This sensitivity analysis applies to one selected appointment. "
    "It does not demonstrate that longer lead times cause no-shows."
)

st.divider()

# --------------------------------------------------
# FAIRNESS ANALYSIS
# --------------------------------------------------
st.header("Fairness Across Age Groups")

fairness_data = pd.DataFrame({
    "Age Group": [
        "0–17",
        "18–34",
        "35–49",
        "50–64",
        "65+"
    ],

    "Actual No-Show Rate (%)": [
        21.36,
        23.65,
        20.95,
        17.38,
        15.46
    ],

    "Predicted Rate Before Mitigation (%)": [
        52.90,
        59.90,
        50.35,
        20.31,
        12.06
    ],

    "Predicted Rate After Removing Age (%)": [
        49.06,
        53.48,
        49.84,
        42.05,
        35.88
    ]
})

st.bar_chart(
    fairness_data.set_index("Age Group")[
        [
            "Actual No-Show Rate (%)",
            "Predicted Rate Before Mitigation (%)",
            "Predicted Rate After Removing Age (%)"
        ]
    ]
)

st.write(
    "Predicted no-show rates varied substantially across age groups. "
    "Removing Age changed these prediction patterns and reduced some "
    "differences, but disparities remained."
)

f1, f2 = st.columns(2)

with f1:
    st.metric(
        "ROC-AUC",
        "73.83% → 72.61%"
    )

with f2:
    st.metric(
        "Recall",
        "68.92% → 73.36%"
    )

st.caption(
    "Removing a protected attribute does not automatically eliminate "
    "fairness concerns because other variables may contain related "
    "or proxy information."
)

st.divider()

# --------------------------------------------------
# ETHICAL SAFEGUARDS
# --------------------------------------------------
st.header("Ethical Safeguards")

st.markdown(
    """
- **Human oversight:** Model predictions should support healthcare staff rather than replace their judgement.
- **Patient access:** No patient should have an appointment automatically cancelled or be denied healthcare because of predicted no-show risk.
- **Privacy protection:** Patient information should be handled using appropriate privacy and data-governance safeguards.
- **Fairness monitoring:** Prediction patterns should continue to be assessed across demographic groups.
"""
)

# --------------------------------------------------
# LIMITATIONS
# --------------------------------------------------
st.header("Model Limitations")

st.markdown(
    """
- The model produces **false-positive predictions**, meaning some patients who would attend may still be flagged as possible no-shows.
- Differences in predictions across age groups remain a fairness consideration.
- The prototype dataset may not fully represent the actual UPTH patient population.
- Results should not automatically be generalized to UPTH without local validation.
"""
)

st.divider()

# --------------------------------------------------
# BUSINESS INTERPRETATION
# --------------------------------------------------
st.header("Business Interpretation")

st.write(
    "The prototype provides information about patterns associated with "
    "appointment no-show risk. Its outputs can help stakeholders understand "
    "risk patterns, prediction uncertainty, model performance and fairness. "
    "Further local validation, monitoring and stakeholder evaluation would "
    "be necessary to understand its suitability for the UPTH environment."
)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------
st.divider()

st.caption(
    "BAN6800 Capstone Project — Trinitas Chideziri Iwunze | "
    "Nexford University"
)
