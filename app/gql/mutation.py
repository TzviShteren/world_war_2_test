from graphene import ObjectType
from app.gql.mutations.missions_mutations import CreateMission, DeleteMission


class Mutation(ObjectType):
    create_mission = CreateMission.Field()
    delete_mission = DeleteMission.Field()