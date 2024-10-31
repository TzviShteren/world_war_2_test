from graphene import Mutation, Int, String, Boolean, Field

from app.db.database import session_maker
from app.db.models import TargetType
from app.gql.types.target_types_type import TargetTypesType


class CreateTargetTypesType(Mutation):
    class Arguments:
        target_type_id = Int(required=True)
        target_type_name = String()

    success = Boolean()
    target_types = Field(TargetTypesType)

    @staticmethod
    def mutate(root, info, target_type_id, target_type_name):
        with session_maker() as session:
            inserted_target_types = TargetType(target_type_id=target_type_id, target_type_name=target_type_name)
            session.add(inserted_target_types)
            session.commit()
            return CreateTargetTypesType(success=True)


class UpdateTargetTypesType(Mutation):
    class Arguments:
        target_type_id = Int(required=True)
        target_type_name = String()

    success = Boolean()
    target_types = Field(TargetTypesType)

    @staticmethod
    def mutate(root, info, target_type_id, target_type_name):
        with session_maker() as session:
            updated_target_types = session.query(TargetType).get(target_type_id)
            updated_target_types.target_type_name = target_type_name
            session.commit()
            session.refresh(updated_target_types)
            return UpdateTargetTypesType(success=True)
