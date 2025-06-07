from django.shortcuts import render
from .models import Student, Subject, Grade
from django.db.models import Avg

def index(request):
    students = Student.objects.all()
    return render(request, 'tracker/index.html', {'students': students})

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'tracker/subject_list.html', {'subjects': subjects})

def grade_list(request):
    grades = Grade.objects.all()
    return render(request, 'tracker/grade_list.html', {'grades': grades})

def report(request):
    students = Student.objects.all()
    report_data = []
    for student in students:
        avg_score = Grade.objects.filter(student=student).aggregate(Avg('score'))['score__avg']
        report_data.append({
            'student': student,
            'avg_score': round(avg_score, 2) if avg_score else 0,
            })
        return render(request, 'tracker/report.html', {'report_data': report_data})