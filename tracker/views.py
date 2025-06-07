from django.shortcuts import render
from .models import Student

def index(request):
    students = Student.objects.all()
    return render(request, 'tracker/index.html', {'students': students})