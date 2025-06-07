from django.contrib.auth.models import User
from tracker.models import Student, Subject, Grade
from random import randint
from datetime import date

def seed_data():
         # Создаём суперпользователя, если его нет
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')

    Student.objects.all().delete()
    Subject.objects.all().delete()
    Grade.objects.all().delete()

    students_data = [
        ('Иван', 'Петров', 'S001'),
        ('Анна', 'Сидорова', 'S002'),
        ('Мария', 'Иванова', 'S003'),
        ('Алексей', 'Смирнов', 'S004'),
        ('Екатерина', 'Козлова', 'S005'),
        ('Дмитрий', 'Морозов', 'S006'),
        ('Ольга', 'Новикова', 'S007'),
        ('Сергей', 'Васильев', 'S008'),
        ('Татьяна', 'Лебедева', 'S009'),
        ('Павел', 'Кузнецов', 'S010'),
         ]
    students = [Student.objects.create(first_name=f, last_name=l, student_id=sid) for f, l, sid in students_data]

    subjects_data = [
        ('Математика', 'MATH101'),
        ('Физика', 'PHYS101'),
        ('Информатика', 'CS101'),
        ('Литература', 'LIT101'),
        ('История', 'HIST101'),
         ]
    subjects = [Subject.objects.create(name=n, code=c) for n, c in subjects_data]

    for student in students:
        for subject in subjects:
            Grade.objects.create(
                student=student,
                subject=subject,
                score=randint(60, 100)  # Оценки от 60 до 100
                )