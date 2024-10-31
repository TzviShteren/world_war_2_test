from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship


class Mission(Base):
    __tablename__ = 'missions'
    id = Column(Integer, primary_key=True)
    mission_id = Column(Integer, ForeignKey('missions.id'))
    mission_date = Column(String)
    airborne_aircraft = Column(String)
    attacking_aircraft = Column(String)
    bombing_aircraft = Column(String)
    aircraft_returned = Column(String)
    aircraft_failed = Column(String)
    aircraft_damaged = Column(String)
    aircraft_lost = Column(String)
