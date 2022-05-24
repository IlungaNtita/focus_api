import graphene
from graphene_django import DjangoObjectType
from tasks.models import Task


class TaskType(DjangoObjectType):
    """ Types for GroupMembers model
    DjangoObjectType automatically transforms a Django Model into a ObjectType"""
    class Meta:
        model = Task
        fields = ("__all__")


class TaskInput(graphene.InputObjectType):
    """Provides input fields to use in mutations"""
    title = graphene.String()
    description = graphene.String()
    user = graphene.ID()
    hours = graphene.Int()
    minutes = graphene.Int()
    seconds = graphene.Int()
    status = graphene.String()


class TaskCreate(graphene.Mutation):
    """Creating an object for Task."""
    task = graphene.Field(TaskType)

    class Arguments:
        input = TaskInput()

    @staticmethod
    def mutate(self, info, input, **kwargs):
        task = Task(
            title=input.title,
            description=input.description,
            hours=input.hour,
            minutes=input.minute,
            seconds=input.second,
            user=input.user)
        task.save()
        return TaskCreate(task=task)


class Query(graphene.ObjectType):
    """Initializing queries"""
    all_tasks = graphene.List(TaskType)
    task = graphene.Field(
        TaskType, task_id=graphene.Int())

    def resolve_all_tasks(root, info):
        return Task.objects.all()

    def resolve_task(root, info, task_id):
        return Task.objects.get(pk=task_id)

    def resolve_user_task(root, info, task_id):
        return Task.objects.get(pk=task_id)


class Mutation(graphene.ObjectType):
    """Initializing all mutations"""
    task_create = TaskCreate.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
