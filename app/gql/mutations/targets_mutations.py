from graphene import Mutation, Int, String, Boolean, Field

from app.db.database import session_maker
from app.db.models import Target
from app.gql.types.targets_type import TargetsType


class TargetsInput(Mutation):
    target_id = Int(required=True)
    target_industry = String()
    target_priority = Int(required=True)
    mission_id = Int(required=True)
    target_type_id = Int(required=True)
    city_id = Int(required=True)


class CreateTarget(Mutation):
    class Arguments:
        target_input = TargetsInput()

    success = Boolean()
    target = Field(TargetsType)

    @staticmethod
    def mutate(root, info, target_input):
        with session_maker() as session:
            inserted_target = Target(**target_input)
            session.add(inserted_target)
            session.commit()
            return CreateTarget(success=True)
