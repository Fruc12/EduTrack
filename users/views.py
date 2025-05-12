from random import randint

import bcrypt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_not_required
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils import timezone

from .forms import LoginForm, SignUpForm
from .models import Validation, User


# Create your views here.

@login_not_required
def login_user(request):
    msg = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Identifiants invalides'
        else:
            msg = 'Erreur lors de la validation du formulaire'
    else:
        form = LoginForm()
    
    context = {'form': form, 'msg': msg}

    return render(request, "users/login.html", context)

@login_not_required
def register_user(request):
    msg = None

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            is_sent, validation = register_mailer(user)
            if is_sent:
                user.save()
                validation.user = user
                validation.code = bcrypt.hashpw(validation.code.encode(), bcrypt.gensalt()).decode()
                validation.save()
                return redirect('users:validate', user.pk)
            msg = "Erreur a l'envoi du mail de validation"
        else:
            msg = 'Erreur lors de la validation du formulaire'
    else:
        form = SignUpForm()
        
    context = {"form": form, "msg": msg}
    return render(request, "users/register.html", context)

@login_not_required
def validate_user(request, user_pk):
    if request.method == "POST":
        code = request.POST["code"]
        user = get_object_or_404(User, pk=user_pk)
        if timezone.now() >= user.validation.expires_at:
            user.delete()
            print("Le code de d'activation a expiré")
            return redirect("users:register")
        if bcrypt.checkpw(code.encode(), user.validation.code.encode()):
            user.is_active=True
            user.save()
            user.validation.delete()
            return redirect('users:login')
        return redirect('users:validate', user_pk)
    context = {"user":get_object_or_404(User, pk=user_pk)}
    return render(request, "users/register-validation.html", context)

def logout_user(request):
    logout(request)
    return redirect("users:login")

def profile(request):
    context = {}
    return render(request, "users/profile.html", context)

def register_mailer(user):
    code = randint(0, 999999)
    code = f"{code:06}"
    validation = Validation(code=code, user=user)
    subject = "Edutrack Validation Inscription"
    body = render_to_string("mails/register-validation.html", {"validation":validation})
    to = [user.email]
    mail = EmailMessage(subject=subject, body=body, to=to)
    mail.content_subtype = 'html'
    return mail.send(), validation
