from pydantic import BaseModel


class DoctorModel(BaseModel):
    id: int
    name: str
    sector_id: int
