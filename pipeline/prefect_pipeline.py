from prefect import flow, task


@task
def ingest_data():
    """Load the raw appointment dataset."""
    print("Loading Medical Appointment No Shows dataset...")


@task
def clean_data():
    """Clean missing, duplicate, and invalid records."""
    print("Cleaning appointment data...")


@task
def transform_data():
    """Transform variables and create appointment lead time."""
    print("Transforming data and creating appointment lead time...")


@task
def validate_data():
    """Apply data quality validation checks."""
    print("Validating cleaned appointment data...")


@task
def prepare_model_data():
    """Prepare the validated dataset for predictive modeling."""
    print("Preparing model-ready dataset...")


@flow(name="UPTH No-Show Data Pipeline")
def upth_no_show_pipeline():
    ingest_data()
    clean_data()
    transform_data()
    validate_data()
    prepare_model_data()


if __name__ == "__main__":
    upth_no_show_pipeline()
