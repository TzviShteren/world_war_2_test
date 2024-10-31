from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from app.db.models import Base


class Mission(Base):
    __tablename__ = 'missions'
    id = Column(Integer, primary_key=True)
    mission_id = Column(Integer)
    mission_date = Column(Date)
    airborne_aircraft = Column(String)
    attacking_aircraft = Column(String)
    bombing_aircraft = Column(String)
    aircraft_returned = Column(String)
    aircraft_failed = Column(String)
    aircraft_damaged = Column(String)
    aircraft_lost = Column(String)
