from django import forms

from classrooms.models import Course, Classroom
from courses.models import Score
from parents.models import Student

class ScoreForm(forms.ModelForm):
    type = forms.ChoiceField(
        choices=Score.TYPES,
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )
    value = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Entrez la note',
                'min': 0,
                'max': 20,
            }
        )
    )
    ponderation = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Pondération',
                'min': 1,
                'max': 10,
            }
        ),
        initial=1,
    )
    student = forms.ModelChoiceField(
        queryset=Student.objects.none(),
        empty_label="Sélectionnez l'élève...",
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )
    course = forms.ModelChoiceField(
        queryset=Course.objects.none(),
        empty_label="Sélectionnez la matière...",
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )
    )

    def __init__(self, *args, **kwargs):
        classroom_id = kwargs.pop('classroom_pk', None)
        super().__init__(*args, **kwargs)
        # Ici, on filtre les élèves et matières de la classe concernée (optionnel)
        if classroom_id is not None:
            classroom = Classroom.objects.get(pk=classroom_id)
            self.fields['student'].queryset = classroom.students.order_by('name')
            self.fields['course'].queryset = classroom.courses.order_by('name')
        else:
            self.fields['student'].queryset = Student.objects.all()
            self.fields['course'].queryset = Course.objects.all()

    class Meta:
        model = Score
        fields = '__all__'