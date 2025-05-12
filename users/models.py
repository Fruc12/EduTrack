from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


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
    code = models.CharField(max_length=128)
    user = models.OneToOneField (User, on_delete=models.CASCADE, related_name='validation')
    created_at = models.DateTimeField(default=timezone.now)
    expires_at = models.DateTimeField(default=timezone.now()+timezone.timedelta(minutes=10))