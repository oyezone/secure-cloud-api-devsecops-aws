from fastapi import FastAPI, Header, HTTPException
from typing import Optional
from datetime import datetime, timezone

app = FastAPI(
    title="Connected Vehicle Telemetry API",
    description="Toyota-style AppSec + DevSecOps portfolio project",
    version="1.0.0"
)

def utc_now():
    return datetime.now(timezone.utc).isoformat()

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "connected-vehicle-telemetry-api",
        "timestamp": utc_now()
    }

@app.post("/auth/login")
def login():
    return {
        "message": "Login endpoint placeholder",
        "token_type": "bearer",
        "timestamp": utc_now()
    }

@app.post("/telemetry/upload")
def upload_telemetry(payload: dict, x_vehicle_id: Optional[str] = Header(default=None)):
    if not x_vehicle_id:
        raise HTTPException(status_code=400, detail="Missing X-Vehicle-ID header")

    return {
        "message": "Telemetry received",
        "vehicle_id": x_vehicle_id,
        "received_at": utc_now(),
        "payload": payload
    }

@app.get("/vehicle/{vehicle_id}/status")
def get_vehicle_status(vehicle_id: str):
    return {
        "vehicle_id": vehicle_id,
        "status": "active",
        "last_seen": utc_now(),
        "battery_level": 82,
        "region": "us-east-1"
    }

@app.get("/admin/diagnostics")
def admin_diagnostics(authorization: Optional[str] = Header(default=None)):
    if authorization != "Bearer admin-token":
        raise HTTPException(status_code=401, detail="Unauthorized")

    return {
        "message": "Restricted diagnostics access granted",
        "environment": "development",
        "timestamp": utc_now()
    }
