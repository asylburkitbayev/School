from django.db import models
from .utils import validate_phone_number


class Director(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    third_name = models.CharField(max_length=55)
    image = models.ImageField(upload_to='Director/', blank=True, null=True)

    phone = models.CharField(max_length=12,
                             unique=True,
                             validators=[validate_phone_number],
                             help_text='введите свои данные.')

    class Meta:
        ordering = ['first_name']
        verbose_name = 'директор'
        verbose_name_plural = 'директор'

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name} {self.third_name}"

    def save(self, *args, **kwargs):
        self.phone = self.phone.replace(' ', '')
        super().save(*args, **kwargs)


class Headteacher(models.Model):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    third_name = models.CharField(max_length=55)
    image = models.ImageField(upload_to='Head_teacher/', blank=True, null=True)

    phone = models.CharField(max_length=12,
                             unique=True,
                             validators=[validate_phone_number],
                             help_text='введите свои данные.')

    class Meta:
        ordering = ['first_name']
        verbose_name = 'завуч'
        verbose_name_plural = 'завучи'

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name} {self.third_name}"

    def save(self, *args, **kwargs):
        self.phone = self.phone.replace(' ', '')
        super().save(*args, **kwargs)



