from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES = [('school', 'Etablissement'), ('parent', 'Parent')]
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLES, default='school')
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]