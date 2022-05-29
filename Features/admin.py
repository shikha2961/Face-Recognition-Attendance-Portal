import imp
from django.contrib import admin

# Register your models here
from .models import newStudent

admin.site.register(newStudent)