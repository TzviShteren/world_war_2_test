from graphene import ObjectType, Int, String, List, Date, Field

from app.db.database import session_maker
from app.db.models.cities import City


class CityType(ObjectType):
    id = Int(required=True)
