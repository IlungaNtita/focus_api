import graphene
# from .schema.task_schema import schema as task
from .task_schema import schema as task
from .user_schema import schema as user
from .sprint_schema import schema as sprint


class Query(task.Query, sprint.Query, user.Query, graphene.ObjectType):
    pass


class Mutation(task.Mutation, sprint.Mutation, user.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

# schema = graphene.Schema(query=Query)
