import pandas as pd

from pipeline.prefect_pipeline import clean_data, transform_data


def test_clean_data_removes_invalid_age():
    """Check that records with invalid ages are removed."""

    sample_data = pd.DataFrame({
        "Age": [25, -1, 45],
        "No-show": ["No", "Yes", "No"],
        "ScheduledDay": [
            "2016-04-01T08:00:00Z",
            "2016-04-02T08:00:00Z",
            "2016-04-03T08:00:00Z",
        ],
        "AppointmentDay": [
            "2016-04-05T00:00:00Z",
            "2016-04-06T00:00:00Z",
            "2016-04-07T00:00:00Z",
        ],
    })

    cleaned_data = clean_data.fn(sample_data)

    assert cleaned_data["Age"].between(0, 120).all()
    assert len(cleaned_data) == 2


def test_clean_data_removes_duplicates():
    """Check that duplicate appointment records are removed."""

    sample_data = pd.DataFrame({
        "Age": [30, 30],
        "No-show": ["No", "No"],
        "ScheduledDay": [
            "2016-04-01T08:00:00Z",
            "2016-04-01T08:00:00Z",
        ],
        "AppointmentDay": [
            "2016-04-05T00:00:00Z",
            "2016-04-05T00:00:00Z",
        ],
    })

    cleaned_data = clean_data.fn(sample_data)

    assert len(cleaned_data) == 1


def test_transform_data_creates_lead_time():
    """Check that appointment lead time is calculated correctly."""

    sample_data = pd.DataFrame({
        "Age": [35],
        "No-show": ["Yes"],
        "ScheduledDay": pd.to_datetime(["2016-04-01T08:00:00Z"]),
        "AppointmentDay": pd.to_datetime(["2016-04-05T00:00:00Z"]),
    })

    transformed_data = transform_data.fn(sample_data)

    assert "AppointmentLeadTime" in transformed_data.columns
    assert transformed_data["AppointmentLeadTime"].iloc[0] == 4


def test_transform_data_creates_binary_target():
    """Check that the no-show outcome is converted to binary format."""

    sample_data = pd.DataFrame({
        "Age": [35, 42],
        "No-show": ["Yes", "No"],
        "ScheduledDay": pd.to_datetime([
            "2016-04-01T08:00:00Z",
            "2016-04-02T08:00:00Z",
        ]),
        "AppointmentDay": pd.to_datetime([
            "2016-04-05T00:00:00Z",
            "2016-04-06T00:00:00Z",
        ]),
    })

    transformed_data = transform_data.fn(sample_data)

    assert transformed_data["NoShowTarget"].tolist() == [1, 0]
