from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.db.base_class import Base


class Sector(Base):
    __tablename__ = "sectors"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    floor = Column(Integer)
    capacity = Column(Integer)
    occupied = Column(Integer)
    visits_allowed_until = Column(DateTime)

    hospital_id = Column(Integer, ForeignKey("hospitals.id"))
