# Generated by Django 4.1.4 on 2022-12-09 05:34

from django.db import migrations, models
import django.db.models.deletion
import teacher.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=55, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=55, verbose_name='Фамилия')),
                ('third_name', models.CharField(max_length=55, verbose_name='Отчество')),
                ('adress_teacher', models.CharField(max_length=200, verbose_name='Место проживания')),
                ('phone', models.CharField(help_text='Номер должен быть в международном формате.', max_length=12, unique=True, validators=[teacher.utils.validate_phone_number], verbose_name='Номер телефона')),
                ('image', models.ImageField(blank=True, null=True, upload_to='teacher/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учителя',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_lesson', models.CharField(max_length=100, verbose_name='Название урока')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_name', to='teacher.teacher', verbose_name='Учитель')),
            ],
            options={
                'verbose_name': 'Уроки',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]