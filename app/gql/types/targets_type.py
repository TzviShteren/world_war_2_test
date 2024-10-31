from graphene import ObjectType, Int, String, List, Date, Field

from app.db.database import session_maker
from app.db.models.missions import Mission


class TargetsType(ObjectType):
    target_id = Int(required=True)
    target_industry = String()
    target_priority = Int()
    mission_id = Int()
    country_id = Int()
    target_type_id = Int()
    city_id = Int()

    mission = List('app.gql.types.missions_type.MissionType')

    @staticmethod
    def resolve_mission(root, info):
        with session_maker() as session:
            return (session.query(Mission)
                    .filter(Mission.mission_id == root.mission_id)
                    .all())
