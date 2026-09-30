
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(
    title="UPTH No-Show Prediction API",
    description="API prototype for predicting outpatient appointment no-show risk.",
    version="1.0"
)

model = joblib.load("upth_no_show_random_forest.joblib")


class AppointmentInput(BaseModel):
    Gender: str
    Age: int
    Neighbourhood: str
    Scholarship: int
    Hipertension: int
    Diabetes: int
    Alcoholism: int
    Handcap: int
    SMS_received: int
    AppointmentLeadTime: int
    ScheduledDayOfWeek: int
    AppointmentDayOfWeek: int
    ScheduledHour: int


@app.get("/")
def home():
    return {
        "message": "UPTH No-Show Prediction API",
        "status": "running"
    }


@app.post("/predict")
def predict(data: AppointmentInput):

    input_df = pd.DataFrame([data.model_dump()])

    probability = float(
        model.predict_proba(input_df)[0, 1]
    )

    prediction = int(probability >= 0.5)

    return {
        "prediction": prediction,
        "predicted_outcome":
            "No-show" if prediction == 1 else "Attend",
        "no_show_probability": round(probability, 4),
        "decision_support_notice":
            "Prediction is for planning and reminder support only; "
            "it must not be used to automatically cancel or deny care."
    }
