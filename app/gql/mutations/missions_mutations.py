from graphene import Mutation, Int, String, Boolean, Field, InputObjectType, Date, Float

from app.db.database import session_maker
from app.db.models import Mission
from app.gql.types.missions_type import MissionType


class MissionInput(InputObjectType):
    mission_id = Int(required=True)
    mission_date = Date(required=True)
    airborne_aircraft = Float(required=True)
    attacking_aircraft = Float(required=True)
    bombing_aircraft = Float(required=True)
    aircraft_returned = Float(required=True)
    aircraft_failed = Float(required=True)
    aircraft_damaged = Float(required=True)
    aircraft_lost = Float(required=True)


class CreateMission(Mutation):
    class Arguments:
        mission_input = MissionInput()

    success = Boolean()
    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, mission_input):
        with session_maker() as session:
            inserted_mission = Mission(**mission_input)
            session.add(inserted_mission)
            session.commit()
            return CreateMission(success=True)


class DeleteMission(Mutation):
    class Arguments:
        mission_id = Int(required=True)

    success = Boolean()
    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, mission_id):
        with session_maker() as session:
            deleted_mission = session.query(Mission).get(mission_id)
            session.delete(deleted_mission)
            session.commit()
            return DeleteMission(success=True)