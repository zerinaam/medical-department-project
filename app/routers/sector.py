from datetime import datetime

from fastapi import APIRouter

from app.db.session import session
from app.models.doctor import Doctor
from app.models.nurse import Nurse
from app.models.sector import Sector
from app.schemas.sector import SectorModel

router = APIRouter()

# TODO: Make sure to cover cases when you get None value from db (example - sector is None you can not access floor)


@router.get("/hospital/{hospital_id}/sector", description="Retrieve all sectors in hospital.")
async def get_sectors(hospital_id: int):
    return session.query(Sector).filter(Sector.hospital_id == hospital_id).all()


@router.get("/hospital/{hospital_id}/sector/{sector_id}", description="Retrieve sector for provided ID.")
async def get_sector(hospital_id: int, sector_id: int):
    return session.query(Sector).filter(Sector.hospital_id == hospital_id, Sector.id == sector_id).first()


@router.get("/hospital/{hospital_id}/floor/{floor}", description="Retrieve sector by floor.")
async def get_sector_by_floor(hospital_id: int, floor: int):
    return session.query(Sector).filter(Sector.hospital_id == hospital_id, Sector.floor == floor).all()


@router.get("/hospital/{hospital_id}/sector/{sector_name}/floor", description="Retrieve floor by sector name.")
async def get_floor_by_sector_name(hospital_id: int, sector_name: str):

    sector = session.query(Sector).filter(Sector.hospital_id == hospital_id, sector_name.capitalize() == Sector.name).first()
    if sector is None:
        return "Sector name is invalid."
    return sector.floor


@router.get("/hospital/{hospital_id}/floor", description="Retrieve all floors in hospital.")
async def get_floors(hospital_id: int):
    sectors = session.query(Sector).filter(Sector.hospital_id == hospital_id).all()
    maximum = 0
    for sector in sectors:
        if sector.floor > maximum:
            maximum = sector.floor
    return maximum


@router.get("/hospital/{hospital_id}/sector/patients", description="Retrieve number of patients in hospital.")
async def get_patients(hospital_id: int):
    sectors = session.query(Sector).filter(Sector.hospital_id == hospital_id).all()
    patients = 0
    for sector in sectors:
        patients += sector.occupied
    return patients


@router.get("/hospital/{hospital_id}/sector/floor/{floor}/patients", description="Retrieve number of patients by floor.")
async def get_patient_by_floor(hospital_id: int, floor: int):
    sectors = session.query(Sector).filter(Sector.hospital_id == hospital_id, Sector.floor == floor).all()
    patients = 0
    for sector in sectors:
        patients += sector.occupied
    return patients


@router.get("/hospital/{hospital_id}/employees", description="Retrieve number of employees in hospital.")
async def get_employees(hospital_id: int):
    doctors = (
        session.query(Doctor)
        .join(Sector, Doctor.sector_id == Sector.id)
        .filter(Sector.hospital_id == hospital_id)
        .all()
    )
    nurses = (
        session.query(Nurse)
        .join(Sector, Nurse.sector_id == Sector.id)
        .filter(Sector.hospital_id == hospital_id)
        .all()
    )
    return len(doctors) + len(nurses)


@router.get("/hospital/{hopital_id}/employees/{floor}", description="Retrieve number of employees by floor.")
async def get_employees(hospital_id: int, floor: int):
    doctors = (
        session.query(Doctor)
        .join(Sector, Doctor.sector_id == Sector.id)
        .filter(Sector.hospital_id == hospital_id, Sector.floor == floor)
        .all()
    )
    nurses = (
        session.query(Nurse)
        .join(Sector, Nurse.sector_id == Sector.id)
        .filter(Sector.hospital_id == hospital_id, Sector.floor == floor)
        .all()
    )
    return len(doctors) + len(nurses)


@router.get("/hospital/{hospital_id}/sector/{sector_name}/visits", description="Retrieve whether visits are allowed.")
async def are_visits_allowed(hospital_id: int, sector_name: str):
    sector = session.query(Sector).filter(Sector.hospital_id == hospital_id, sector_name.capitalize() == Sector.name).first()

    if sector is None:
        return "Sector name is invalid."
    else:
        if datetime.now().time() <= sector.visits_allowed_until.time():
            return "Visits are allowed."
        return "Visits are not allowed."


@router.get("/hospital/{hospital_id}/empty_beds", description="Retrieve number of empty beds in hospital.")
async def empty_beds(hospital_id: int):
    sectors = session.query(Sector).filter(Sector.hospital_id == hospital_id).all()
    beds = 0
    for sector in sectors:
        beds += sector.capacity - sector.occupied
    return beds


@router.get("/hospital/{hospital_id}/empty_beds/{floor}", description="Retrieve number of empty beds by floor.")
async def empty_beds(hospital_id: int, floor: int):
    sectors = session.query(Sector).filter(Sector.hospital_id == hospital_id, floor == Sector.floor).all()
    beds = 0
    for sector in sectors:
        beds += sector.capacity - sector.occupied
    return beds


@router.post("/sector", description="Create new sector.")
async def create_sector(sector_model: SectorModel):
    sector = Sector(
        id=sector_model.id,
        name=sector_model.name,
        hospital_id=sector_model.hospital_id,
        floor=sector_model.floor,
        capacity=sector_model.capacity,
        occupied=sector_model.occupied,
        visits_allowed_until=sector_model.visits_allowed_until.isoformat(),
    )
    session.add(sector)
    session.commit()
    return "Sector created."
