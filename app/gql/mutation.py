from graphene import ObjectType
from app.gql.mutations.missions_mutations import CreateMission, DeleteMission
from app.gql.mutations.targets_mutations import CreateTarget
from app.gql.mutations.target_types_mutations import CreateTargetTypesType, UpdateTargetTypesType


class Mutation(ObjectType):
    create_mission = CreateMission.Field()
    delete_mission = DeleteMission.Field()
    create_target = CreateTarget.Field()
    create_target_types = CreateTargetTypesType.Field()
    update_targets_types = UpdateTargetTypesType.Field()
