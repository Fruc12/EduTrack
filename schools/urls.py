from django.urls import path, include
from . import views

app_name = 'schools'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('list/', views.index_school, name='index'),
    path('<int:pk>/delete/', views.delete_school, name='delete'),
    path('<int:school_pk>/classrooms/', include('classrooms.urls')),
]
