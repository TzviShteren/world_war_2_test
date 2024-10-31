from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    country_id = Column(Integer, ForeignKey('countries.id'))
    country_name = Column(String)