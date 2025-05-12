from django.urls import path
from . import views

app_name = "classrooms"
urlpatterns = [
    path('', views.index_classrooms, name='index'),
    path('<int:classroom_pk>/', views.show_classroom, name='show'),
    path('<int:classroom_pk>/add_student', views.add_student, name='add_student'),
    path('<int:classroom_pk>/add_parent', views.add_parent, name='add_parent'),
    path('<int:classroom_pk>/delete/', views.delete_classroom, name='delete'),
]