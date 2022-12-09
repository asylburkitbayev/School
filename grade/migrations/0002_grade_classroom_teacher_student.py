# Generated by Django 4.1.4 on 2022-12-09 06:18

from django.db import migrations, models
import django.db.models.deletion
import teacher.utils


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
        ('grade', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='classroom_teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teacher.teacher', verbose_name='Классная руководительница'),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=55, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=55, verbose_name='Фамилия')),
                ('third_name', models.CharField(max_length=55, verbose_name='Отчество')),
                ('parents_phone', models.CharField(help_text='Номер должен быть в международном формате.', max_length=12, unique=True, validators=[teacher.utils.validate_phone_number], verbose_name='Телефон родителей')),
                ('location', models.CharField(max_length=55, verbose_name='Место проживания')),
                ('image', models.ImageField(blank=True, null=True, upload_to='student/', verbose_name='Фото')),
                ('klass', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_grade', to='grade.grade', verbose_name='Класс')),
            ],
        ),
    ]