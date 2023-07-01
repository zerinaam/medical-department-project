from pydantic import BaseModel


class HospitalModel(BaseModel):
    id: int
    name: str
    building_year: int
    sectors: list

