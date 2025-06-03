from django import forms

from schools.models import School, SchoolYear
from .models import Classroom

class ClassroomForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nom de la classe",
                "class": "form-control"
            }
        ))
    level = forms.ChoiceField(
        choices=Classroom.LEVELS,
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ))

    school_year = forms.ModelChoiceField(queryset=SchoolYear.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ))

    class Meta:
        model = Classroom
        fields = ('name', 'level', 'school_year')