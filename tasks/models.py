from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=False)
    icon = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1, null=True, blank=True)
    hours = models.IntegerField(null=True, blank=True, default=0)
    minutes = models.IntegerField(null=True, blank=True, default=0)
    seconds = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.title
