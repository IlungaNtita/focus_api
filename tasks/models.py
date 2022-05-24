from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    TASK_STATUS = [
        ("TODO", 'To Do'),
        ("IN_PROGRESS", 'In Progress'),
        ("DONE", 'Done'),
    ]

    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=20, choices=TASK_STATUS,
                              default="TODO", null=True, blank=True)
    icon = models.CharField(max_length=255, null=True,
                            blank=True, default="⭕️")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hours = models.IntegerField(null=True, blank=True, default=0)
    minutes = models.IntegerField(null=True, blank=True, default=0)
    seconds = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.title
