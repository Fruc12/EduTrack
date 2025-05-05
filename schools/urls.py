from django.urls import path
from . import views

app_name = 'schools'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('schools/', views.index_school, name='index'),
    path('schools/<int:pk>/', views.show_school, name='show'),
    path('schools/<int:pk>/delete/', views.delete_school, name='delete'),
]
