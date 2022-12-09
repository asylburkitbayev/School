from django.db import models
from director.models import Director, Headteacher
from teacher.models import Teacher, Lesson
from grade.models import Student, Grade


class Mekteb(models.Model):
    director = models.OneToOneField(Director, on_delete=models.SET_NULL, null=True, verbose_name='Директор')
    head_teacher = models.ForeignKey(Headteacher, on_delete=models.SET_NULL, null=True, verbose_name='Завуч')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, verbose_name='Учитель')
    klass = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True, verbose_name='Классы')
    students = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True, verbose_name='Ученики')
    lessons = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, verbose_name='Уроки')

    class Meta:
        ordering = ['klass']
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'
