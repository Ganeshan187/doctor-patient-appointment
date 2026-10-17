
from fastapi import FastAPI

app = FastAPI(title="Doctor Appointment API")


@app.get("/health")
def health_check():
    return {"status": "ok"}
