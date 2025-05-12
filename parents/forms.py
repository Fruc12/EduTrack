from django import forms

from classrooms.models import Classroom
from .models import Parent, Student

class StudentForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Nom de l'élève",
            }
        )
    )
    classroom = forms.ModelChoiceField(
        queryset=Classroom.objects.all(),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    class Meta:
        model = Student
        fields = ['name', 'classroom']

class ParentForm(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Prénom du parent",
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Nom du parent",
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Email du parent",
            }
        )
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': "Téléphone du parent",
            }
        )
    )
    student = forms.ModelChoiceField(
        queryset=Student.objects.all(),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    class Meta:
        model = Parent
        fields = ['name', 'email', 'phone', 'student']