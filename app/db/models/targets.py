from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db.models import Base


class Target(Base):
    __tablename__ = 'targets'
    target_id = Column(Integer, primary_key=True, autoincrement=True)
    target_industry = Column(String, nullable=False)
    target_priority = Column(Integer, nullable=False)
    mission_id = Column(Integer, ForeignKey("missions.mission_id"))
    country_id = Column(Integer, ForeignKey("countries.country_id"))
    target_type_id = Column(Integer, ForeignKey("target_types.target_type_id"))
    city_id = Column(Integer, ForeignKey("cities.city_id"))

    target_type = relationship("TargetType", back_populates="targets")
    city = relationship("City", back_populates="targets")
    mission = relationship("Mission", back_populates="targets")