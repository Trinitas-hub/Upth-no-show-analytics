def evaluate_retraining_trigger(
    psi,
    demographic_parity_difference,
    disparate_impact_ratio,
    current_recall=None,
    baseline_recall=None
):
    """
    Evaluate whether the UPTH no-show model requires human review
    and possible retraining.

    This function does NOT automatically retrain or deploy a model.
    It creates a review trigger for responsible human oversight.
    """

    reasons = []

    # Data-drift trigger
    if psi > 0.25:
        reasons.append(
            "Significant data drift detected (PSI > 0.25)."
        )
    elif psi >= 0.10:
        reasons.append(
            "Moderate data drift detected (PSI >= 0.10)."
        )

    # Fairness triggers
    if demographic_parity_difference > 0.10:
        reasons.append(
            "Demographic parity difference exceeded 0.10."
        )

    if disparate_impact_ratio < 0.80:
        reasons.append(
            "Disparate impact ratio fell below 0.80."
        )

    # Performance degradation trigger
    if (
        current_recall is not None
        and baseline_recall is not None
        and current_recall < baseline_recall - 0.05
    ):
        reasons.append(
            "Recall decreased by more than 0.05 from baseline."
        )

    if reasons:
        return {
            "triggered": True,
            "status": "Human review required",
            "reasons": reasons,
            "recommended_action": (
                "Investigate data quality, drift, fairness and model "
                "performance. Retraining may proceed only after review "
                "and approval by authorized project stakeholders."
            )
        }

    return {
        "triggered": False,
        "status": "Continue monitoring",
        "reasons": [],
        "recommended_action": (
            "No retraining action required. Continue routine monitoring."
        )
    }


if __name__ == "__main__":
    # Synthetic demonstration only.
    # These values do not represent live UPTH production monitoring.
    result = evaluate_retraining_trigger(
        psi=0.28,
        demographic_parity_difference=0.06,
        disparate_impact_ratio=0.87,
        current_recall=0.70,
        baseline_recall=0.78
    )

    print("UPTH No-Show Model Retraining Review")
    print(result)
