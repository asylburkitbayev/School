from django.contrib.auth.models import User
from django.db import models


class Grade(models.Model):
    littera = models.CharField(max_length=2, verbose_name='Буква класса')
    number_of_grade = models.PositiveIntegerField(verbose_name='Номер класса')
    # classroom_teacher: Teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True,
    #                                                verbose_name='Классная руководительница')

    def __str__(self):
        return f'{self.number_of_grade} {self.littera}'

    class Meta:
        ordering = ['number_of_grade']
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'
