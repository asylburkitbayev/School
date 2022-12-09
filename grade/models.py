from django.contrib.auth.models import User
from django.db import models
from teacher.models import Teacher
from teacher.utils import validate_phone_number, validate_grade


class Grade(models.Model):
    littera = models.CharField(max_length=1, verbose_name='Буква класса')
    number_of_grade = models.PositiveIntegerField(validators=[validate_grade],verbose_name='Номер класса')
    classroom_teacher: Teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True,
                                                   verbose_name='Классная руководительница')

    def save(self, *args, **kwargs):
        self.littera = self.littera.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.number_of_grade} {self.littera}'

    class Meta:
        ordering = ['number_of_grade']
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


class Student(models.Model):
    first_name = models.CharField(max_length=55, verbose_name='Имя')
    last_name = models.CharField(max_length=55, verbose_name='Фамилия')
    third_name = models.CharField(max_length=55, verbose_name='Отчество')
    klass = models.OneToOneField(Grade, on_delete=models.CASCADE, related_name= 'student_grade', verbose_name='Класс')
    parents_phone = models.CharField(max_length=12, unique=True, validators=[validate_phone_number],
                                     help_text='Номер должен быть в международном формате.',
                                     verbose_name='Телефон родителей')
    location = models.CharField(max_length=55, verbose_name='Место проживания')
    image = models.ImageField(upload_to='student/', blank=True, null=True, verbose_name='Фото')

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.third_name}'

    class Meta:
        ordering = ['klass']
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'
