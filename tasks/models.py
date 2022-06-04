from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    TASK_STATUS = [
        (u"To Do", u'To Do'),
        (u"In Progress", u'In Progress'),
        (u"Done", u'Done'),
    ]

    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=20,
                              default="To Do", null=True, blank=False)
    icon = models.CharField(max_length=255, null=True,
                            blank=True, default="⭕️")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1, null=True, blank=True)
    hours = models.IntegerField(null=True, blank=True, default=0)
    minutes = models.IntegerField(null=True, blank=True, default=0)
    seconds = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.title
