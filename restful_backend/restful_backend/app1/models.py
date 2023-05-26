from distutils.command.upload import upload
from django.db import models

# Create your models here.
class LoginInfo(models.Model):
    userName = models.CharField(max_length=100)
    passWd = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.userName


class FileModel(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to = 'upload')

