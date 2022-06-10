from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
active_roles = (
    ("premium", "premium"),
    ("trial", "trial")
)


class DescripableModel(models.Model):
    class Meta:
        """Metadata for the Describable Model."""
        abstract = True

    def __init__(self, *args, **kwargs):
        """Initialize the Describable model."""
        super().__init__(*args, **kwargs)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)


class TimestampableModel(models.Model):
    """Add timestamps to model."""

    class Meta:
        """Metadata for the Timestampable Model."""
        abstract = True

    def __init__(self, *args, **kwargs):
        """Initialize the Timestampable model."""
        super(TimestampableModel, self).__init__(*args, **kwargs)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=120, choices=active_roles, default="premium")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Sprint(DescripableModel, TimestampableModel):
    STATUS = (
        ("ACTIVE", "Active"),
        ("COMPLETED", "Completed"),
    )
    status = models.CharField(max_length=20, null=True,
                              choices=STATUS, default="ACTIVE", blank=False)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1, null=True, blank=True)

    def __str__(self):
        return self.title


class Task(DescripableModel, TimestampableModel):
    status = models.CharField(max_length=20, null=True, blank=False)
    icon = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1, null=True, blank=True)
    hours = models.IntegerField(null=True, blank=True, default=0)
    minutes = models.IntegerField(null=True, blank=True, default=0)
    seconds = models.IntegerField(null=True, blank=True, default=0)
    task_sprint = models.ForeignKey(
        Sprint, on_delete=models.CASCADE, default=1, null=True, blank=True)

    def __str__(self):
        return self.title
