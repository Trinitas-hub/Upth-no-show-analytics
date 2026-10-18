import pytest

from monitoring.drift_monitor import calculate_psi
from monitoring.fairness_monitor import (
    selection_rate,
    demographic_parity_difference,
    disparate_impact_ratio,
)
from monitoring.retraining_trigger import evaluate_retraining_trigger


def test_calculate_psi_no_drift():
    reference = [10, 20, 30, 40, 50]
    current = [10, 20, 30, 40, 50]

    psi = calculate_psi(reference, current)

    assert psi >= 0
    assert psi < 0.10


def test_selection_rate():
    predictions = [1, 0, 1, 1, 0]

    rate = selection_rate(predictions)

    assert rate == pytest.approx(0.6)


def test_demographic_parity_difference():
    group_a = [1, 1, 0, 0]
    group_b = [1, 0, 0, 0]

    difference = demographic_parity_difference(group_a, group_b)

    assert difference == pytest.approx(0.25)


def test_disparate_impact_ratio():
    group_a = [1, 1, 0, 0]
    group_b = [1, 0, 0, 0]

    ratio = disparate_impact_ratio(group_a, group_b)

    assert ratio == pytest.approx(0.5)


def test_retraining_trigger_for_significant_drift():
    result = evaluate_retraining_trigger(
        psi=0.30,
        demographic_parity_difference=0.05,
        disparate_impact_ratio=0.90,
    )

    assert result["review_required"] is True


def test_retraining_trigger_no_alert():
    result = evaluate_retraining_trigger(
        psi=0.05,
        demographic_parity_difference=0.05,
        disparate_impact_ratio=0.90,
    )

    assert result["review_required"] is False
