from django.contrib import admin
# from django.utils.safestring import mark_safe
from .models import Grade


class GradeAdmin(admin.ModelAdmin):
    list_display = ['littera', 'number_of_grade']


admin.site.register(Grade, GradeAdmin)
