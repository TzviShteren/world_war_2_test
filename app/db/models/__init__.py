from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .missions import Mission
from .countries import Country
from .city import City
from .targets import Target
from .target_types import TargetType

