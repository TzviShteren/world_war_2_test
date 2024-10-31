from graphene import ObjectType, Int, String, List, Date, Field, Float

from app.db.database import session_maker
from app.db.models.targets import Target


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

    target = Field('app.gql.types.targets_type.TargetsType')

    @staticmethod
    def resolve_target(root, info):
        with session_maker() as session:
            return (session.query(Target)
                    .filter(Target.mission_id == root.mission_id)
                    .first())
