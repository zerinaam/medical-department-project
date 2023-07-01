from fastapi import APIRouter
from app.db.session import session
from app.models.doctor import Doctor
from app.models.sector import Sector
from app.schemas.doctor import DoctorModel

router = APIRouter()


@router.get("/hospital_id/{hospital_id}/doctors", description="Retrieve all doctors.")
async def get_all_doctors(hospital_id: int):
    doctors = session.query(Doctor).join(Sector, Doctor.sector_id == Sector.id).filter(Sector.hospital_id == hospital_id).all()
    return doctors


@router.get("/hospital_id/{hospital_id}/doctor/{doctor_id}", description="Retrieve doctor by id.")
async def get_doctor_by_id(hospital_id: int, doctor_id: int):
    doctor = (
        session.query(Doctor)
        .join(Sector, Doctor.sector_id == Sector.id)
        .filter(Sector.hospital_id == hospital_id, Doctor.id == doctor_id)
        .first()
    )
    return doctor


@router.post("/doctor", description="Add new doctor.")
async def create_doctor(doctor_model: DoctorModel):
    doctor = Doctor(
        id=doctor_model.id,
        name=doctor_model.name,
        sector_id=doctor_model.sector_id
    )
    session.add(doctor)
    session.commit()
    return "Doctor is added."
