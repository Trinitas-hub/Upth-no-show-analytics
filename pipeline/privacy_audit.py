from pathlib import Path
from datetime import datetime, timezone
import csv


LOG_PATH = Path("reports/privacy_audit_log.csv")


def log_privacy_event(action, dataset, details):
    """Record privacy-related data processing activities."""

    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

    file_exists = LOG_PATH.exists()

    with LOG_PATH.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "timestamp_utc",
                "action",
                "dataset",
                "details",
            ])

        writer.writerow([
            datetime.now(timezone.utc).isoformat(),
            action,
            dataset,
            details,
        ])


def create_privacy_audit_log():
    """Document privacy controls applied to the appointment dataset."""

    log_privacy_event(
        action="Dataset accessed",
        dataset="processed_appointments.csv",
        details="Processed appointment dataset accessed for privacy preparation.",
    )

    log_privacy_event(
        action="Direct identifiers removed",
        dataset="processed_appointments.csv",
        details="PatientId and AppointmentID removed before analytical use.",
    )

    log_privacy_event(
        action="Anonymized output created",
        dataset="anonymized_appointments.csv",
        details="Privacy-prepared dataset created with direct identifiers removed.",
    )

    log_privacy_event(
        action="Access restriction documented",
        dataset="anonymized_appointments.csv",
        details="Analytical dataset intended for authorized project use only.",
    )

    print("Privacy audit events recorded successfully.")
    print(f"Audit log saved to {LOG_PATH}.")


if __name__ == "__main__":
    create_privacy_audit_log()
