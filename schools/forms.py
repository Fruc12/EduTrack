from django import forms
from django.shortcuts import get_object_or_404

from .models import School, SchoolYear

CHOICES = [ ('semester', 'Semestre')]
class SchoolForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nom de votre école",
                "class": "form-control"
            }
        ))
    period = forms.ChoiceField(
        choices=School.PERIODS,
        widget=forms.Select(
            attrs={
                "class": "form-control"
            }
        ))
    class Meta:
        model = School
        fields = '__all__'

class SchoolYearForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ex: 2023-2024 ",
                "class": "form-control"
            }
        )
    )
    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type' : 'date',
            }
        )
    )
    end_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type' : 'date',
            }
        )
    )
    school = forms.ModelChoiceField(
        queryset=School.objects.all(),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    class Meta:
        model = SchoolYear
        fields = '__all__'

class ChangeYearForm(forms.Form):
    school_years = forms.ModelChoiceField(
        queryset=SchoolYear.objects.none(),  # Initialisé vide
        widget=forms.Select(
            attrs={
                'class': 'form-control',
            }
        )  # widget adapté
    )

    def __init__(self, *args, **kwargs):
        school_id = kwargs.pop('school_pk', None)  # Récupération de school_id
        super().__init__(*args, **kwargs)
        self.fields['school_years'].queryset = get_object_or_404(School, pk=school_id).schoolYears.order_by("-name")


# class SignUpForm(UserCreationForm):
#     first_name = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder": "Prénom",
#                 "class": "form-control"
#             }
#         ))
#     last_name = forms.CharField(
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder": "Nom",
#                 "class": "form-control"
#             }
#         ))
#     email = forms.EmailField(
#         widget=forms.EmailInput(
#             attrs={
#                 "placeholder": "Email",
#                 "class": "form-control"
#             }
#         ))
#     password1 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "placeholder": "Mot de passe",
#                 "class": "form-control"
#             }
#         ))
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "placeholder": "Confirmer le mot de passe",
#                 "class": "form-control"
#             }
#         ))
#
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        # labels = {
        #     'username': 'Nom d\'utilisateur',
        #     'email': 'Email',
        #     'password1': 'Mot de passe',
        #     'password2': 'Confirmer le mot de passe'
        # }