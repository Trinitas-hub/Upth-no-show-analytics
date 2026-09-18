from pathlib import Path

import pandas as pd
from prefect import flow, task


DATA_PATH = Path("data/KaggleV2-May-2016.csv")
OUTPUT_PATH = Path("data/processed_appointments.csv")


@task
def ingest_data():
    """Load the Medical Appointment No Shows dataset."""
    df = pd.read_csv(DATA_PATH)
    print(f"Loaded {len(df)} appointment records.")
    return df


@task
def clean_data(df):
    """Clean duplicate, missing, and invalid records."""
    df = df.copy()

    # Remove duplicate records
    df = df.drop_duplicates()

    # Remove records with missing target values
    df = df.dropna(subset=["No-show"])

    # Remove invalid age values
    df = df[df["Age"].between(0, 120)]

    # Convert appointment dates to datetime
    df["ScheduledDay"] = pd.to_datetime(df["ScheduledDay"], errors="coerce")
    df["AppointmentDay"] = pd.to_datetime(df["AppointmentDay"], errors="coerce")

    # Remove records with invalid appointment dates
    df = df.dropna(subset=["ScheduledDay", "AppointmentDay"])

    print(f"{len(df)} records remain after cleaning.")
    return df


@task
def transform_data(df):
    """Create features required for later predictive modeling."""
    df = df.copy()

    # Create appointment lead time in days
    df["AppointmentLeadTime"] = (
        df["AppointmentDay"].dt.normalize()
        - df["ScheduledDay"].dt.normalize()
    ).dt.days

    # Remove records with impossible negative lead time
    df = df[df["AppointmentLeadTime"] >= 0]

    # Convert the no-show target to binary format
    df["NoShowTarget"] = df["No-show"].map({"Yes": 1, "No": 0})

    print("Appointment lead time and model target created.")
    return df


@task
def validate_data(df):
    """Apply basic quality checks before model preparation."""

    assert df["No-show"].notna().all(), "Missing no-show values detected."
    assert df["Age"].between(0, 120).all(), "Invalid age values detected."
    assert df["AppointmentLeadTime"].ge(0).all(), "Invalid lead time detected."
    assert df["NoShowTarget"].isin([0, 1]).all(), "Invalid target values detected."

    print("Basic data quality checks passed.")
    return df


@task
def prepare_model_data(df):
    """Save the validated dataset for predictive modeling."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    print(f"Model-ready dataset saved to {OUTPUT_PATH}.")
    return str(OUTPUT_PATH)


@flow(name="UPTH No-Show Data Pipeline")
def upth_no_show_pipeline():
    raw_data = ingest_data()
    clean_data_result = clean_data(raw_data)
    transformed_data = transform_data(clean_data_result)
    validated_data = validate_data(transformed_data)
    prepare_model_data(validated_data)


if __name__ == "__main__":
    upth_no_show_pipeline()
