from fastapi import APIRouter

from app.db.session import session
from app.models.hospital import Hospital
from app.schemas.hospital import HospitalModel

router = APIRouter()


@router.get("/hospital", description="Retrieve all hospitals.")
async def get_hospitals():
    return session.query(Hospital).all()


@router.get("/hospital/{id}", description="Retrieve hospital for provided ID.")
async def get_hospital(id: int):
    hospital = session.query(Hospital).filter(Hospital.id == id).first()
    return hospital


@router.get("/hospital/{id}/building_year", description="Retrieve building year for provided ID.")
async def get_building_year(id: int):
    hospital = session.query(Hospital).filter(Hospital.id == id).first()
    return hospital.building_year


@router.post("/hospital", description="Create new hospital.")
async def create_hospital(hospital_model: HospitalModel):
    hospital = Hospital(
        id=hospital_model.id,
        name=hospital_model.name,
        building_year=hospital_model.building_year
    )
    session.add(hospital)
    session.commit()
    return "Hospital created."

