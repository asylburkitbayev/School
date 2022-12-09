from django.db import models
from .utils import validate_phone_number


class Teacher(models.Model):
    first_name = models.CharField(max_length=55, verbose_name='Имя')
    last_name = models.CharField(max_length=55, verbose_name='Фамилия')
    third_name = models.CharField(max_length=55, verbose_name='Отчество')
    adress_teacher = models.CharField(max_length=200, verbose_name='Место проживания')
    phone = models.CharField(max_length=12,
                             unique=True,
                             validators=[validate_phone_number],
                             help_text='Номер должен быть в международном формате.',
                             verbose_name='Номер телефона')
    image = models.ImageField(upload_to='teacher/', blank=True, null=True, verbose_name='Фото')

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'

    @property
    def full_name(self):
        return (f"{self.first_name} {self.last_name} {self.first_name}")

    def save(self, *args, **kwargs):
        self.phone = self.phone.replace(' ', '')
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)



class Lesson(models.Model):
    name_lesson = models.CharField(max_length=100, verbose_name='Название урока')
    teacher: Teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_name', verbose_name='Учитель')

    class Meta:
        verbose_name = 'Уроки'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.name_lesson
