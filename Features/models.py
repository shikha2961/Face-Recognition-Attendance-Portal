from distutils.command.upload import upload
from django.db import models

# Create your models here.

# Model to store the data of newStudent added 
class newStudent(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to = '', default="")

    def __str__(self):
        return self.name