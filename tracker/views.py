from django.shortcuts import render, redirect
from .models import Student, Subject, Grade
from .forms import StudentForm, GradeForm
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
    subjects = Subject.objects.all()
    report_data = []
    for student in students:
        avg_score = Grade.objects.filter(student=student).aggregate(Avg('score'))['score__avg']
        report_data.append({
            'student': student,
            'avg_score': round(avg_score, 2) if avg_score else 0,
        })
    best_student = max(report_data, key=lambda x: x['avg_score'], default=None)
    worst_student = min(report_data, key=lambda x: x['avg_score'], default=None)
    subject_avgs = [
        {
            'subject': subject,
            'avg_score': round(Grade.objects.filter(subject=subject).aggregate(Avg('score'))['score__avg'] or 0, 2)
        }
        for subject in subjects
    ]
    return render(request, 'tracker/report.html', {
        'report_data': sorted(report_data, key=lambda x: x['avg_score'], reverse=True),
        'best_student': best_student,
        'worst_student': worst_student,
        'subject_avgs': subject_avgs,
    })

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tracker:index')
    else:
        form = StudentForm()
    return render(request, 'tracker/student_form.html', {'form': form})
def grade_create(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tracker:grade_list')
    else:
        form = GradeForm()
    return render(request, 'tracker/grade_form.html', {'form': form})