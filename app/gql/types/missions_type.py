from graphene import ObjectType, Int, String, List, Date, Field, Float

from app.db.database import session_maker
from app.db.models.missions import Mission


class MissionType(ObjectType):
    mission_id = Int(required=True)
    mission_date = Date()
    airborne_aircraft = String()
    attacking_aircraft = String()
    bombing_aircraft = String()
    aircraft_returned = String()
    aircraft_failed = String()
    aircraft_damaged = String()
    aircraft_lost = String()