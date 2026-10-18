import json
from datetime import datetime, timezone
from pathlib import Path


STORE_PATH = Path("monitoring/explanations.jsonl")


def save_explanation(
    prediction_id,
    predicted_class,
    predicted_probability,
    feature_contributions,
    model_version="prototype"
):
    """
    Store an explanation record for audit and review.

    feature_contributions can contain SHAP values or another
    approved explanation representation.

    No directly identifying patient information should be stored.
    """

    record = {
        "prediction_id": str(prediction_id),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "model_version": model_version,
        "predicted_class": int(predicted_class),
        "predicted_probability": float(predicted_probability),
        "feature_contributions": feature_contributions
    }

    STORE_PATH.parent.mkdir(parents=True, exist_ok=True)

    with STORE_PATH.open("a", encoding="utf-8") as file:
        file.write(json.dumps(record) + "\n")

    return record


def load_explanations():
    """
    Load stored explanation records for authorized audit or review.
    """

    if not STORE_PATH.exists():
        return []

    records = []

    with STORE_PATH.open("r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                records.append(json.loads(line))

    return records


if __name__ == "__main__":
    # Synthetic demonstration only.
    # No real patient information is used.
    example = save_explanation(
        prediction_id="DEMO-001",
        predicted_class=1,
        predicted_probability=0.72,
        feature_contributions={
            "lead_time_days": 0.18,
            "age": -0.07,
            "sms_received": -0.05
        },
        model_version="UPTH-no-show-prototype-v1"
    )

    print("Explanation stored successfully.")
    print(example)
