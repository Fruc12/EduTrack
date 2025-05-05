from django import forms
from .models import School

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
                "placeholder": "Mot de passe",
                "class": "form-control"
            }
        ))
    class Meta:
        model = School
        fields = '__all__'


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