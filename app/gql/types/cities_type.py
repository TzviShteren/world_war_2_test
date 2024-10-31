from graphene import ObjectType, Int, String, List, Date, Field, Float

from app.db.database import session_maker
from app.db.models.cities import City


class CityType(ObjectType):
    city_id = Int(required=True)
    city_name = String()
    longitude = Float()
    latitude = Float()
    country_id = Int(required=True)
