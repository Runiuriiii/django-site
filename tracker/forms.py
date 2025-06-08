from django import forms
from .models import Student, Grade

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'student_id']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'student_id': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            }

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'subject', 'score']
        widgets = {
                 'student': forms.Select(attrs={'class': 'w-full p-2 border rounded'}),
                 'subject': forms.Select(attrs={'class': 'w-full p-2 border rounded'}),
                 'score': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded', 'step': '0.1', 'min': '0', 'max': '100'}),
             }