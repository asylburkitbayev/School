# Generated by Django 4.1.4 on 2022-12-09 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0002_grade_classroom_teacher_student'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['klass'], 'verbose_name': 'Ученик', 'verbose_name_plural': 'Ученики'},
        ),
    ]
