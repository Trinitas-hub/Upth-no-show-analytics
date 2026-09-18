from pathlib import Path

import pandas as pd


DATA_PATH = Path("data/processed_appointments.csv")


def load_processed_data():
    """Load the cleaned and validated appointment dataset."""
    df = pd.read_csv(DATA_PATH)
    print(f"Loaded {len(df)} processed appointment records.")
    return df


def assess_gender_representation(df):
    """Assess representation and no-show rates by gender."""
    gender_summary = (
        df.groupby("Gender")
        .agg(
            Appointment_Count=("Gender", "size"),
            No_Show_Rate=("NoShowTarget", "mean"),
        )
        .reset_index()
    )

    gender_summary["Representation_Percent"] = (
        gender_summary["Appointment_Count"] / len(df) * 100
    )

    return gender_summary


def assess_age_representation(df):
    """Assess representation and no-show rates across age groups."""
    df = df.copy()

    age_bins = [0, 17, 34, 49, 64, 120]
    age_labels = [
        "0-17",
        "18-34",
        "35-49",
        "50-64",
        "65+",
    ]

    df["AgeGroup"] = pd.cut(
        df["Age"],
        bins=age_bins,
        labels=age_labels,
        include_lowest=True,
    )

    age_summary = (
        df.groupby("AgeGroup", observed=False)
        .agg(
            Appointment_Count=("AgeGroup", "size"),
            No_Show_Rate=("NoShowTarget", "mean"),
        )
        .reset_index()
    )

    age_summary["Representation_Percent"] = (
        age_summary["Appointment_Count"] / len(df) * 100
    )

    return age_summary


def main():
    """Run the demographic representation assessment."""
    df = load_processed_data()

    print("\nGENDER REPRESENTATION AND NO-SHOW RATES")
    print(assess_gender_representation(df).to_string(index=False))

    print("\nAGE-GROUP REPRESENTATION AND NO-SHOW RATES")
    print(assess_age_representation(df).to_string(index=False))

    print(
        "\nThese results are descriptive checks of representation "
        "and outcome patterns. They do not establish model bias."
    )


if __name__ == "__main__":
    main()
