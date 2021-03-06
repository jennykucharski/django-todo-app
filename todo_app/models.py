from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class User(AbstractUser):
    date_of_birth = models.DateField(blank=True, null=True)


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='notes',
        on_delete=models.CASCADE
    )

    class Meta:
        abstract = True


class Note(Base):
    name  = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()

    def __str__(self):
        return self.name
