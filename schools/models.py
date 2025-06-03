from django.db import models

from users.models import User


class School(models.Model):
    PERIODS = [ ('','Sélectionnez une période'), ('trimester', 'Trimestre'), ('semester', 'Semestre') ]
    name = models.CharField(max_length=50)
    period = models.CharField(max_length=50, choices=PERIODS)

class SchoolYear(models.Model):
    name = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='schoolYears')

    def __str__(self):
        return self.name

class SchoolUser(models.Model):
    ROLES = [ ('','Sélectionnez une un role'), ('director', 'Directeur'), ('staff', "Personnel d'administration")]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='schoolUsers')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='schoolUsers')
    role = models.CharField(choices=ROLES, max_length=20)