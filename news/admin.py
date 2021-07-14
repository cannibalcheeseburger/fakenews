from django.contrib import admin
from .models import News,UnratedNews
# Register your models here.

admin.site.register(News),
admin.site.register(UnratedNews),