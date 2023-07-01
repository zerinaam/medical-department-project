from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base_class import Base


class Nurse(Base):
    __tablename__ = "nurses"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    sector_id = Column(Integer, ForeignKey("sectors.id"))
