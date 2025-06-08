from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.index, name='index'),
    path('subjects/', views.subject_list, name='subject_list'),
    path('grades/', views.grade_list, name='grade_list'),
    path('report/', views.report, name='report'),
    path('students/create/', views.student_create, name='student_create'),
    path('students/<int:pk>/edit/', views.student_edit, name='student_edit'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('grades/create/', views.grade_create, name='grade_create'),
    path('grades/<int:pk>/edit/', views.grade_edit, name='grade_edit'),
    path('grades/<int:pk>/delete/', views.grade_delete, name='grade_delete'),
    ]