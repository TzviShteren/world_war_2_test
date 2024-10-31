from graphene import ObjectType, Int, String, List, Date, Field

from app.db.database import session_maker
from app.db.models.missions import Mission

class MissionType(ObjectType):
    id = Int(required=True)