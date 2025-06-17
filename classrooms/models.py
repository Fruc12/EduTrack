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

class Course(models.Model):
    name = models.CharField(max_length=100)
    coef = models.IntegerField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.name

class TimeTable(models.Model):
    DAYS = [ ('', 'Veuillez choisir un jour de la semaine...'), (0, 'Lundi'), (1, 'Mardi'), (2, 'Mercredi'), (3, 'Jeudi'), (4, 'Vendredi'), (5, 'Samedi') ]
    # name = models.CharField(max_length=256)
    day = models.IntegerField(choices=DAYS)
    begin_time = models.TimeField()
    end_time = models.TimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='timeTables')

    def __str__(self):
        return str(self.begin_time) + ' ' + str(self.day)