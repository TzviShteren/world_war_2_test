from graphene import ObjectType, Int, String, List, Date, Field

from app.db.database import session_maker
from app.db.models.countries import Country

class CountryType(ObjectType):
    id = Int(required=True)
