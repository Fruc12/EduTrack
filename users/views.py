from django.contrib.auth.decorators import login_not_required
from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

@login_not_required
def login_user(request):
    form = msg = None
    context = {}
    
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
    msg = form = None

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("users:login")

        else:
            msg = 'Erreur lors de la validation du formulaire'
    else:
        form = SignUpForm()
        
    context = {"form": form, "msg": msg}
    return render(request, "users/register.html", context)

def logout_user(request):
    logout(request)
    return redirect("users:login")

def profile(request):
    context = {}
    return render(request, "users/profile.html", context)