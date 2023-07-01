from datetime import datetime

from pydantic import BaseModel


class SectorModel(BaseModel):
    id: int
    name: str
    hospital_id: int
    floor: int
    capacity: int
    occupied: int
    visits_allowed_until: datetime
