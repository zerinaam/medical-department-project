from sqlalchemy import Column, Integer, String, ForeignKey, ARRAY

from app.db.base_class import Base


class Hospital(Base):
    __tablename__ = "hospitals"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    building_year = Column(Integer)




