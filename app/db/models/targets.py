from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship


class Target(Base):
    __tablename__ = 'targets'
    id = Column(Integer, primary_key=True)
    target_id = Column(Integer, ForeignKey('targets.id'))
    mission_id = Column(Integer, ForeignKey('missions.id'))
    target_industry = Column(String)
    city_id = Column(Integer, ForeignKey('citys.id'))
    target_type_id = Column(Integer, ForeignKey('target_types.id'))
    target_priority = Column(Integer)