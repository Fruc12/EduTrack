from django.db import models

from schools.models import School, SchoolYear


class Classroom(models.Model):
    LEVELS = [ ('', 'Veuillez choisir un niveau'),
               ('6','Sixième'),('5','Cinquième'),('4','Quatrième'),('3','Troisième'),
               ('2','Seconde'),('1','Première'),('Tle','Terminale')
    ]
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=10, choices=LEVELS)
    school_year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE, related_name='classrooms')

    def __str__(self):
        return self.name