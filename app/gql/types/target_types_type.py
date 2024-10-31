from graphene import ObjectType, Int, String, List, Date, Field

from app.db.database import session_maker
from app.db.models.target_types import TargetType

class TargetTypesType(ObjectType):
    id = Int(primary_key=True)
