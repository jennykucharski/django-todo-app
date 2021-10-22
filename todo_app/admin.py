from django.contrib import admin
from .models import Note, User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class UserAdmin(BaseUserAdmin):
    ordering = ('email',)
    list_filter = ('is_admin',)

admin.site.register(Note)
admin.site.register(User, UserAdmin)
