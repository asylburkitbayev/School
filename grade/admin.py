from django.contrib import admin
# from django.utils.safestring import mark_safe
from .models import Grade, Student


class GradeAdmin(admin.ModelAdmin):
    list_display = ['littera', 'number_of_grade']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['klass', 'last_name']


admin.site.register(Grade, GradeAdmin)
admin.site.register(Student, StudentAdmin)
