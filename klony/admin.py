from django.contrib import admin

# Register your models here.
from klony.models import Acers, Post, Image


@admin.register(Acers)
class AcersAdmin(admin.ModelAdmin):
    list_display = ('latin_name', 'type', 'variant', 'image_tree')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'text')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'caption')
