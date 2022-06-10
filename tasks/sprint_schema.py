import graphene
from graphene_django import DjangoObjectType
from tasks.models import Sprint


class SprintType(DjangoObjectType):
    """ Types for GroupMembers model
    DjangoObjectType automatically transforms a Django Model into a ObjectType"""
    class Meta:
        model = Sprint
        fields = ("__all__")


class SprintInput(graphene.InputObjectType):
    """Provides input fields to use in mutations"""
    title = graphene.String()
    description = graphene.String()
    user = graphene.ID()
    status = graphene.String()


class SprintCreate(graphene.Mutation):
    """Creating an object for Sprint."""
    sprint = graphene.Field(SprintType)

    class Arguments:
        input = SprintInput()

    @staticmethod
    def mutate(self, info, input, **kwargs):
        sprint = Sprint(
            title=input.title,
            description=input.description,
            status=input.status,
            user_id=input.user)
        sprint.save()
        return SprintCreate(sprint=sprint)


class SprintUpdate(graphene.Mutation):
    """Creating an object for Sprint."""
    sprint = graphene.Field(SprintType)

    class Arguments:
        input = SprintInput()
        id = graphene.ID(
            required=True, description="ID of a sprint to update.")

    @staticmethod
    def mutate(self, info, id, input, **kwargs):
        sprint = Sprint.objects.get(id=id)
        sprint.title = input.title
        sprint.description = input.description
        sprint.status = input.status
        sprint.save()
        # Notice we return an instance of this mutation
        return SprintUpdate(sprint=sprint)


class SprintDelete(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, **kwargs):
        obj = Sprint.objects.get(pk=kwargs["id"])
        obj.delete()
        return cls(ok=True)


class Query(graphene.ObjectType):
    """Initializing queries"""
    all_sprints = graphene.List(SprintType)
    sprint = graphene.Field(
        SprintType, sprint_id=graphene.Int())
    user_sprint = graphene.Field(
        SprintType, user_id=graphene.Int())

    def resolve_all_sprints(root, info):
        return Sprint.objects.all()

    def resolve_sprint(root, info, sprint_id):
        return Sprint.objects.get(pk=sprint_id)

    def resolve_user_sprint(root, info, user_id):
        return Sprint.objects.get(user_id=user_id)


class Mutation(graphene.ObjectType):
    """Initializing all mutations"""
    sprint_create = SprintCreate.Field()
    sprint_update = SprintUpdate.Field()
    sprint_delete = SprintDelete.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
