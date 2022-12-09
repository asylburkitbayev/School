from django.contrib import admin
from .models import Teacher, Lesson

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'adress_teacher', 'phone']

class LessonAdmin(admin.ModelAdmin):
    list_display = ['name_lesson', 'teacher']


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Lesson, LessonAdmin)
