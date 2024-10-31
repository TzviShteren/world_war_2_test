from graphene import ObjectType, Int, String, List, Date, Field, Float

from app.db.database import session_maker
from app.db.models.missions import Mission


class MissionType(ObjectType):
    mission_id = Int(required=True)
    mission_date = Date()
    airborne_aircraft = Float()
    attacking_aircraft = Float()
    bombing_aircraft = Float()
    aircraft_returned = Float()
    aircraft_failed = Float()
    aircraft_damaged = Float()
    aircraft_lost = Float()