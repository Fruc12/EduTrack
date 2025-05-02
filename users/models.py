from django.db import models
from django.contrib.auth.models import AbstractUser

ROLES = [('school', 'Établissement'), ('parent', 'Parent')]

class User(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(choices=ROLES, default='school')
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]