from fastapi import APIRouter
from app.db.session import session
from app.models.hospital import Hospital
from app.models.nurse import Nurse
from app.models.sector import Sector
from app.schemas.nurse import NurseModel

router = APIRouter()


@router.get("/hospital_id{hospital_id}/nurse", description="Retrieve all nurses.")
async def get_all_doctors(hospital_id: int):
    nurses = session.query(Nurse).join(Sector, Nurse.sector_id == Sector.id).filter(Sector.hospital_id == hospital_id).all()
    return nurses


@router.get("/hospital_id{hospital_id}/nurse/{nurse_id}", description="Retrieve nurse by id.")
async def get_nurse_by_id(hospital_id: int, nurse_id: int):
    nurse = (
        session.query(Nurse)
        .join(Sector, Nurse.sector_id == Sector.id)
        .filter(Sector.hospital_id == hospital_id, Nurse.id == nurse_id)
        .first()
    )
    return nurse


@router.post("/nurse", description="Add new nurse.")
async def create_doctor(nurse_model: NurseModel):
    nurse = Nurse(
        id=nurse_model.id,
        name=nurse_model.name,
        sector_id=nurse_model.sector_id
    )
    session.add(nurse)
    session.commit()
    return "Nurse is added."
