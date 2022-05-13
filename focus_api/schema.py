import graphene
from tasks.schema import schema as tasks


class Query(tasks.Query, graphene.ObjectType):
    pass


class Mutation(tasks.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
