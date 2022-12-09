# Generated by Django 4.1.4 on 2022-12-09 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('director', '0002_headteacher'),
        ('grade', '0003_alter_student_options'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mekteb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='director.director', verbose_name='Директор')),
                ('head_teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='director.headteacher', verbose_name='Завуч')),
                ('klass', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='grade.grade', verbose_name='Классы')),
                ('lessons', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teacher.lesson', verbose_name='Уроки')),
                ('students', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='grade.student', verbose_name='Ученики')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teacher.teacher', verbose_name='Учитель')),
            ],
            options={
                'verbose_name': 'Школа',
                'verbose_name_plural': 'Школы',
                'ordering': ['klass'],
            },
        ),
    ]