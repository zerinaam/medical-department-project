from pydantic import BaseModel


class NurseModel(BaseModel):
    id: int
    name: str
    sector_id: int
