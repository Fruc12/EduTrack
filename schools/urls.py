from django.urls import path
from . import views

app_name = 'schools'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]
