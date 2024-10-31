from graphene import ObjectType, Int, String, List, Date, Field

from app.db.database import session_maker
from app.db.models.targets import Target


class TargetsType(ObjectType):
    target_id = Int(required=True)
    target_industry = String()
    target_priority = Int()
    mission_id = Int()
    country_id = Int()
    target_type_id = Int()
    city_id = Int()


