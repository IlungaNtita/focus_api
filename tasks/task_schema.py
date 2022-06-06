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
    icon = graphene.String()


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
            hours=input.hours,
            status=input.status,
            icon=input.icon,
            minutes=input.minutes,
            seconds=input.seconds,
            user_id=input.user)
        task.save()
        return TaskCreate(task=task)


class TaskUpdate(graphene.Mutation):
    """Creating an object for Task."""
    task = graphene.Field(TaskType)

    class Arguments:
        input = TaskInput()
        id = graphene.ID(
            required=True, description="ID of a task to update.")

    @staticmethod
    def mutate(self, info, id, input, **kwargs):
        task = Task.objects.get(id=id)
        if input.hours == None:
            task.title = input.title
            task.description = input.description
            task.save()
        else:
            task.title = input.title
            task.description = input.description
            task.hours = input.hours
            task.minutes = input.minutes
            task.seconds = input.seconds
            task.icon = input.icon
            task.status = input.status
            task.save()
        # Notice we return an instance of this mutation
        return TaskUpdate(task=task)


class TaskUpdateTime(graphene.Mutation):
    """Creating an object for Task."""
    task = graphene.Field(TaskType)

    class Arguments:
        input = TaskInput()
        id = graphene.ID(
            required=True, description="ID of a task to update.")

    @staticmethod
    def mutate(self, info, id, input, **kwargs):
        task = Task.objects.get(id=id)
        task.hours = input.hours
        task.minutes = input.minutes
        task.seconds = input.seconds
        task.icon = input.icon
        task.status = input.status
        task.save()
        # Notice we return an instance of this mutation
        return TaskUpdate(task=task)


class TaskDelete(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, **kwargs):
        obj = Task.objects.get(pk=kwargs["id"])
        obj.delete()
        return cls(ok=True)


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
    task_update = TaskUpdate.Field()
    task_delete = TaskDelete.Field()
    task_update_time = TaskUpdateTime.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
