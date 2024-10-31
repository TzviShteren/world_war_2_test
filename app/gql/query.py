from graphene import ObjectType, List, Field, Int, String, Date

from app.db.models import Mission, Target
# from app.gql.types.user_type import UserType

from app.db.database import session_maker


class Query(ObjectType):
    # query 1
    mission_by_id = Field(Mission, mission_id=Int())

    # query 2
    mission_by_date_range = List(Mission, start_date=Date(), end_date=Date())

    # query 3
    mission_by_country = List(Target, country=String())

    # query 4

    # query 5

    # query 6

    @staticmethod
    def resolve_mission_by_id(root, info, mission_id):
        with session_maker() as session:
            mission = (session.query(Mission)
                       .filter(Mission.mission_id == mission_id)
                       .first())

    @staticmethod
    def resolve_mission_by_date_range(root, info, start_date, end_date):
        with session_maker() as session:
            mission = (session.query(Mission)
                       .filter(Mission.mission_date >= start_date and Mission.mission_date <= end_date)
                       .all())

    @staticmethod
    def resolve_mission_by_country(root, info, country):
        with session_maker() as session:
            mission = (session.query(Mission).filter)
