from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Task, profile, Sprint
from django.contrib import admin

# Register your models here.
# Inline + descriptor


class AdminProfileInline(admin.StackedInline):
    model = profile
    can_delete = False
    verbose_name_plural = 'profiles'

# Define new admin with inline


class ProfileUserAdmin(BaseUserAdmin):
    inlines = (AdminProfileInline,)


# Re-register UserAdmin
admin.site.register(Task)
admin.site.register(Sprint)
admin.site.unregister(User)
admin.site.register(User, ProfileUserAdmin)
