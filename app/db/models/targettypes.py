from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

class TargetType(Base):
    __tablename__ = 'targettypes'
    id = Column(Integer, primary_key=True)
    target_type_id = Column(Integer, ForeignKey('targettypes.id'))
    target_type_name = Column(String)
