import graphene
# from .schema.task_schema import schema as task
from .task_schema import schema as task


class Query(task.Query, graphene.ObjectType):
    pass


class Mutation(task.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

# schema = graphene.Schema(query=Query)
