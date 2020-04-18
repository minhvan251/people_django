from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
# Register your models here.
class InlineProfile(admin.StackedInline):
    model = Profile

class UserProfile(admin.ModelAdmin):
    inlines = [
        InlineProfile,
    ]

admin.site.register(Profile)
admin.site.unregister(User)
admin.site.register(User,UserProfile)
