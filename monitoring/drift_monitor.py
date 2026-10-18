import numpy as np
import pandas as pd


def calculate_psi(reference, current, bins=10):
    """
    Calculate Population Stability Index (PSI) to detect
    changes between reference and current numeric data.
    """

    reference = pd.Series(reference).dropna().astype(float)
    current = pd.Series(current).dropna().astype(float)

    if reference.empty or current.empty:
        raise ValueError("Reference and current data must not be empty.")

    # Create bins from the reference distribution
    breakpoints = np.unique(
        np.quantile(reference, np.linspace(0, 1, bins + 1))
    )

    if len(breakpoints) < 2:
        return 0.0

    breakpoints[0] = -np.inf
    breakpoints[-1] = np.inf

    reference_counts, _ = np.histogram(reference, bins=breakpoints)
    current_counts, _ = np.histogram(current, bins=breakpoints)

    reference_pct = reference_counts / len(reference)
    current_pct = current_counts / len(current)

    # Prevent division by zero or log(0)
    epsilon = 0.0001
    reference_pct = np.where(reference_pct == 0, epsilon, reference_pct)
    current_pct = np.where(current_pct == 0, epsilon, current_pct)

    psi_values = (
        (current_pct - reference_pct)
        * np.log(current_pct / reference_pct)
    )

    return float(np.sum(psi_values))


def classify_drift(psi):
    """
    Interpret PSI using the monitoring thresholds
    defined for the UPTH no-show prototype.
    """

    if psi < 0.10:
        return "No significant drift"

    if psi <= 0.25:
        return "Moderate drift - investigate"

    return "Significant drift - model review required"


def monitor_feature(reference, current, feature_name):
    """
    Calculate PSI for one feature and return a monitoring result.
    """

    psi = calculate_psi(reference, current)

    return {
        "feature": feature_name,
        "psi": round(psi, 4),
        "status": classify_drift(psi)
    }


if __name__ == "__main__":
    # Demonstration only.
    # These values are synthetic and are not UPTH production data.
    reference_data = [10, 12, 15, 18, 20, 22, 25, 28, 30, 35]
    current_data = [11, 13, 16, 19, 21, 24, 27, 31, 34, 38]

    result = monitor_feature(
        reference_data,
        current_data,
        "Example feature"
    )

    print("UPTH No-Show Drift Monitoring Demonstration")
    print(result)
