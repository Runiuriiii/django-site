from django.db import models
class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    student_id = models.CharField(max_length=10, unique=True, verbose_name='ID студента')
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Meta:
    verbose_name = 'Студент'
    verbose_name_plural = 'Студенты'

class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    code = models.CharField(max_length=10, unique=True, verbose_name='Код предмета')

    def __str__(self):
        return self.name

class Meta:
    verbose_name = 'Предмет'
    verbose_name_plural = 'Предметы'
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades', verbose_name='Студент')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='grades', verbose_name='Предмет')
    score = models.FloatField(verbose_name='Оценка')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return f"{self.student} - {self.subject}: {self.score}"

class Meta:
    verbose_name = 'Оценка'
    verbose_name_plural = 'Оценки'
