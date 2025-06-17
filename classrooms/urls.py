from django.urls import path
from . import views

app_name = "classrooms"
urlpatterns = [
    path('', views.index_classrooms, name='index'),
    path('year/', views.add_school_year, name='add_year'),
    path('<int:classroom_pk>/', views.show_classroom, name='show'),
    path('<int:classroom_pk>/add_student/', views.add_student, name='add_student'),
    path('<int:classroom_pk>/add_parent/', views.add_parent, name='add_parent'),
    path('<int:classroom_pk>/add_course/', views.add_course, name='add_course'),
    path('<int:classroom_pk>/add_time_table/', views.add_time_table, name='add_time_table'),
    path('<int:classroom_pk>/delete/', views.delete_classroom, name='delete'),
]