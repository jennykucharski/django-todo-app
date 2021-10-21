from django.db import models
from django.contrib import admin

class Base(models.Model):
    created_at = models.DateTimeField()
    created_by = models.CharField(max_length=200)
    modified_at = models.DateTimeField()
    class Meta:
        abstract = True


class Note(Base):
    name  = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

