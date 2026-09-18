from pathlib import Path

import great_expectations as gx
import pandas as pd


DATA_PATH = Path("data/processed_appointments.csv")


def load_data():
    """Load the Medical Appointment No Shows dataset."""
    df = pd.read_csv(DATA_PATH)
    print(f"Loaded {len(df)} appointment records.")
    return df


def validate_appointment_data(df):
    """Validate key data-quality requirements using Great Expectations."""

    context = gx.get_context()

    data_source = context.data_sources.add_pandas("appointment_data_source")
    data_asset = data_source.add_dataframe_asset(name="appointment_data")

    batch_definition = data_asset.add_batch_definition_whole_dataframe(
        "appointment_batch"
    )

    batch = batch_definition.get_batch(batch_parameters={"dataframe": df})

    suite = gx.ExpectationSuite(name="appointment_data_quality_suite")

    # Required fields should not contain missing values
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToNotBeNull(column="No-show")
    )

    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToNotBeNull(column="Age")
    )

    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToNotBeNull(column="ScheduledDay")
    )

    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToNotBeNull(column="AppointmentDay")
    )

    # Age should remain within an acceptable range
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToBeBetween(
            column="Age",
            min_value=0,
            max_value=120,
        )
    )

    # No-show should contain only expected categories
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToBeInSet(
            column="No-show",
            value_set=["Yes", "No"],
        )
    )

    # Gender should contain only expected dataset categories
    suite.add_expectation(
        gx.expectations.ExpectColumnValuesToBeInSet(
            column="Gender",
            value_set=["F", "M"],
        )
    )

    validation_results = batch.validate(suite)

    print(validation_results)

    if validation_results.success:
        print("DATA QUALITY GATE: PASSED")
    else:
        print("DATA QUALITY GATE: FAILED")

    return validation_results


if __name__ == "__main__":
    appointment_data = load_data()
    validate_appointment_data(appointment_data)
