from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from app.db.models import Base


class Mission(Base):
    __tablename__ = 'missions'
    mission_id = Column(Integer, primary_key=True, autoincrement=True)
    mission_date = Column(Date, nullable=False)
    airborne_aircraft = Column(String, nullable=False)
    attacking_aircraft = Column(String, nullable=False)
    bombing_aircraft = Column(String, nullable=False)
    aircraft_returned = Column(String, nullable=False)
    aircraft_failed = Column(String, nullable=False)
    aircraft_damaged = Column(String, nullable=False)
    aircraft_lost = Column(String, nullable=False)

    targets = relationship('Target', back_populates='mission')