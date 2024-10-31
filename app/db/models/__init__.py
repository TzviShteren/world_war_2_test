from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .missions import Mission
from .targets import Target
from .target_types import TargetType
from .cities import City
from .countries import Country
