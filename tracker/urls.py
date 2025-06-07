from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.index, name='index'),
    path('subjects/', views.subject_list, name='subject_list'),
    path('grades/', views.grade_list, name='grade_list'),
    path('report/', views.report, name='report'),
    ]