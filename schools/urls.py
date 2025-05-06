from django.urls import path
from . import views

app_name = 'schools'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('list/', views.index_school, name='index'),
    path('<int:pk>/', views.show_school, name='show'),
    path('<int:pk>/delete/', views.delete_school, name='delete'),
]
