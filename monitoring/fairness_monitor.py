import pandas as pd


def selection_rate(predictions):
    """
    Calculate the proportion of predictions classified as no-show risk.
    Predictions should contain 0 or 1 values.
    """
    predictions = pd.Series(predictions).dropna()

    if predictions.empty:
        raise ValueError("Predictions must not be empty.")

    return float(predictions.mean())


def demographic_parity_difference(group_a, group_b):
    """
    Calculate the absolute difference in selection rates
    between two demographic groups.
    """
    rate_a = selection_rate(group_a)
    rate_b = selection_rate(group_b)

    return abs(rate_a - rate_b)


def disparate_impact_ratio(group_a, group_b):
    """
    Calculate the ratio between the lower and higher
    selection rates of two demographic groups.
    """
    rate_a = selection_rate(group_a)
    rate_b = selection_rate(group_b)

    higher_rate = max(rate_a, rate_b)
    lower_rate = min(rate_a, rate_b)

    if higher_rate == 0:
        return 1.0

    return lower_rate / higher_rate


def classify_fairness(dpd, di_ratio):
    """
    Flag results that may require human fairness review.

    These thresholds are monitoring triggers, not automatic
    decisions that a model is fair or unfair.
    """
    if dpd <= 0.10 and di_ratio >= 0.80:
        return "Within monitoring threshold"

    return "Fairness review required"


def monitor_fairness(group_a, group_b, group_a_name, group_b_name):
    """
    Return fairness-monitoring results for two groups.
    """
    rate_a = selection_rate(group_a)
    rate_b = selection_rate(group_b)

    dpd = demographic_parity_difference(group_a, group_b)
    di_ratio = disparate_impact_ratio(group_a, group_b)

    return {
        "group_a": group_a_name,
        "group_b": group_b_name,
        "group_a_selection_rate": round(rate_a, 4),
        "group_b_selection_rate": round(rate_b, 4),
        "demographic_parity_difference": round(dpd, 4),
        "disparate_impact_ratio": round(di_ratio, 4),
        "status": classify_fairness(dpd, di_ratio)
    }


if __name__ == "__main__":
    # Demonstration only.
    # These predictions are synthetic and are not UPTH production data.
    group_a_predictions = [1, 0, 1, 0, 1, 0, 0, 1, 0, 1]
    group_b_predictions = [1, 0, 0, 0, 1, 0, 0, 1, 0, 0]

    result = monitor_fairness(
        group_a_predictions,
        group_b_predictions,
        "Example Group A",
        "Example Group B"
    )

    print("UPTH No-Show Fairness Monitoring Demonstration")
    print(result)
