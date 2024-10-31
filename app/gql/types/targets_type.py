from graphene import ObjectType, Int, String, List, Date, Field

from app.db.database import session_maker
from app.db.models.targets import Target

class TargetsType(ObjectType):
    id = Int(required=True)
