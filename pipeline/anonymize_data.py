from pathlib import Path

import pandas as pd


INPUT_PATH = Path("data/processed_appointments.csv")
OUTPUT_PATH = Path("data/anonymized_appointments.csv")

IDENTIFIER_COLUMNS = ["PatientId", "AppointmentID"]


def anonymize_data():
    """Remove direct identifiers from the processed appointment dataset."""

    df = pd.read_csv(INPUT_PATH)

    print(f"Loaded {len(df)} processed appointment records.")

    columns_to_remove = [
        column for column in IDENTIFIER_COLUMNS
        if column in df.columns
    ]

    df = df.drop(columns=columns_to_remove)

    print("Removed identifier columns:", columns_to_remove)

    df.to_csv(OUTPUT_PATH, index=False)

    print(f"Anonymized dataset saved to {OUTPUT_PATH}.")
    print(f"Final number of records: {len(df)}")

    return df


if __name__ == "__main__":
    anonymize_data()
