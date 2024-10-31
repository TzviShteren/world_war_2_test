from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db.models import Base


class TargetType(Base):
    __tablename__ = 'target_types'
    id = Column(Integer, primary_key=True)
    target_type_id = Column(Integer)
    target_type_name = Column(String)
