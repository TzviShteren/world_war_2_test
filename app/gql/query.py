from graphene import ObjectType, List, Field, Int, String, Date

from app.db.models import Mission, Target, TargetType
from app.gql.types.missions_type import MissionType
from app.gql.types.targets_type import TargetsType
from app.gql.types.cities_type import City
from app.gql.types.countries_type import Country

from app.db.database import session_maker


class Query(ObjectType):
    # query 1
    mission_by_id = Field(MissionType, mission_id=Int())

    # query 2
    mission_by_date_range = List(MissionType, start_date=Date(), end_date=Date())

    # query 3
    mission_by_country = List(MissionType, country=String())

    # query 4
    mission_by_target_industry = List(MissionType, target_industry=String())

    # query 5 (I didn't do the task, because it doesn't make sense)
    # aircraft_by_mission = List(MissionType, aircraft_mission=String())

    # query 6
    mission_by_target_type = List(MissionType, target_type=String())

    @staticmethod
    def resolve_mission_by_id(root, info, mission_id):
        with session_maker() as session:
            return session.get(Mission, mission_id)

    @staticmethod
    def resolve_mission_by_date_range(root, info, start_date, end_date):
        if start_date < end_date:
            return None
        with session_maker() as session:
            return (
                session.query(Mission)
                .filter(
                    Mission.mission_date >= start_date,
                    Mission.mission_date <= end_date
                )
                .all()
            )

    @staticmethod
    def resolve_mission_by_country(root, info, country):
        with session_maker() as session:
            return (
                session.query(Mission)
                .join(Target)
                .join(City)
                .join(Country)
                .filter(Country.country_name == country)
                .all()
            )

    @staticmethod
    def resolve_mission_by_target_industry(root, info, target_industry):
        with session_maker() as session:
            return (session.query(Mission)
                    .filter(Target.target_industry == target_industry)
                    .all())

    @staticmethod
    def resolve_mission_by_target_type(root, info, target_type):
        with session_maker() as session:
            return (
                session.query(Mission)
                .join(Target)
                .join(TargetType)
                .filter(TargetType.target_type_name == target_type)
                .all()
            )