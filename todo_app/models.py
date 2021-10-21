from django.db import models
from django.contrib import admin



class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200)
    modified_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class Note(Base):
    name  = models.CharField(max_length=100, blank=True, default='')
    content = models.TextField()
    def __str__(self):
        return self.name
