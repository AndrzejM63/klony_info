from django.contrib import admin

# Register your models here.
from klony.models import Acers


@admin.register(Acers)
class AcersAdmin(admin.ModelAdmin):
    list_display = ('latin_name', 'type', 'variant', 'image_tree')
