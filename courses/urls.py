from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path('<int:course_pk>/', views.index_course, name='index'),
]