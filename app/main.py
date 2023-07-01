from fastapi import FastAPI

from app.routers import hospital, sector, doctor, nurse

app = FastAPI(
    title="Medical Department",
    version="0.1.0",
)

app.include_router(hospital.router)
app.include_router(sector.router)
app.include_router(doctor.router)
app.include_router(nurse.router)
