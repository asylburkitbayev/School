from django.contrib import admin
# from django.utils.safestring import mark_safe
from .models import Mekteb


class MektebAdmin(admin.ModelAdmin):
    list_display = ['director', 'head_teacher', 'teacher', 'klass', 'students', 'lessons']


admin.site.register(Mekteb, MektebAdmin)
