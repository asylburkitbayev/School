from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Director


class DirectorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'third_name']

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} width='100' height='110'")


admin.site.register(Director, DirectorAdmin)


