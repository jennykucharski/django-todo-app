from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager that will allow
    using email as unique identifier
    """
    def create_user(self, email, password, **extra_fields):
        """
        Knowing with did all of this just to normalize the
        email there no point of processing the other fields,
        hence the use of **extra_fields to squeeze them inside.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(_('email address'), unique=True)
    date_of_birth = models.DateField()
    username = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    def  __str__(self):
        return f"{self.first_name}, {self.last_name} - {self.email}"


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
