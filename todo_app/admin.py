from django.contrib import admin
# from .models import Note, User
from .models import Note
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.admin import UserAdmin
# Register your models here.

# class UserAdmin(BaseUserAdmin):
    # ordering = ('email',)
    # list_filter = ('is_admin',)

admin.site.register(Note)
# admin.site.register(User, UserAdmin)


