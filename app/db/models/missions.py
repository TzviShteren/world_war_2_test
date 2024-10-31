from sqlalchemy import Column, Integer, Float, Date
from sqlalchemy.orm import relationship
from app.db.models import Base


class Mission(Base):
    __tablename__ = 'missions'
    mission_id = Column(Integer, primary_key=True, autoincrement=True)
    mission_date = Column(Date, nullable=False)
    airborne_aircraft = Column(Float, nullable=False)
    attacking_aircraft = Column(Float, nullable=False)
    bombing_aircraft = Column(Float, nullable=False)
    aircraft_returned = Column(Float, nullable=False)
    aircraft_failed = Column(Float, nullable=False)
    aircraft_damaged = Column(Float, nullable=False)
    aircraft_lost = Column(Float, nullable=False)

    targets = relationship('Target', back_populates='mission')