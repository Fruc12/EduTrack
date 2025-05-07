from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username_validator = True

    username = models.CharField(max_length=1, blank=True, null=True)
    ROLES = [('school', 'Etablissement'), ('parent', 'Parent')]
    email = models.EmailField(unique=True, max_length=255)
    role = models.CharField(max_length=20, choices=ROLES, default='school')
    is_active = models.BooleanField(default=False)
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

class Validation(models.Model):
    code = models.IntegerField()
    user = models.OneToOneField (User, on_delete=models.CASCADE, related_name='validation')
    created_at = models.DateTimeField(default=datetime.now())
    expires_at = models.DateTimeField(default=datetime.now()+timedelta(minutes=10))