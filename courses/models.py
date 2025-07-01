from django.db import models

from classrooms.models import Course
from parents.models import Student


class Score(models.Model):
    TYPES = [
        ('', 'Sélectionner le type...'),
        ('control', 'Contrôle'),
        ('exam', 'Devoir'),
    ]
    value = models.IntegerField()
    type = models.CharField(max_length=100, choices=TYPES)
    ponderation = models.IntegerField(blank=True, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    # student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='scores')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='scores')

    def __str__(self):
        return self.value
