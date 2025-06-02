from django.db import models

from classrooms.models import Classroom
from users.models import User


class Student(models.Model):
    name = models.CharField(max_length=70)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='students')

class Parent(models.Model):
    phone = models.CharField(max_length=10)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='parent')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='parent')
