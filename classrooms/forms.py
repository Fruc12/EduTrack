from django import forms
from django.shortcuts import get_object_or_404

from schools.models import SchoolYear
from .models import Classroom, Course, TimeTable


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
        )
    )

    school_year = forms.ModelChoiceField(queryset=SchoolYear.objects.all(),
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = Classroom
        fields = '__all__'

class CourseForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nom de la matière",
                "class": "form-control"
            }
        )
    )
    coef = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Coefficient"
            }
        )
    )
    classroom = forms.ModelChoiceField(queryset=Classroom.objects.all())

    class Meta:
        model = Course
        fields = '__all__'

class TimeTableForm(forms.ModelForm):
    course = forms.ModelChoiceField(
        queryset=Course.objects.none(),
        empty_label="Choisissez une matière...",
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )
    day = forms.ChoiceField(
        choices=TimeTable.DAYS,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )
    begin_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                'class': 'form-control',
                # 'placeholder': 'Heure début',
                'type': 'time'
            }
        )
    )
    end_time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                'class': 'form-control',
                # 'placeholder': 'Heure fin',
                'type': 'time'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        classroom_id = kwargs.pop('classroom_pk', None)
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = get_object_or_404(Classroom, pk=classroom_id).courses.order_by("name")

    class Meta:
        model = TimeTable
        fields = '__all__'