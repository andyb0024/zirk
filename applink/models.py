# from email.mime import image
from django.db import models
#
#
# # Create your models here.
# class AppLink(models.Model):
#     name = models.CharField(max_length=16,default=False)
#     image = models.ImageField(upload_to='app/')
#
#     def __str__(self):
#         return f'{self.name}'

class AppLink(models.Model):
    name=models.CharField(max_length=16)
    image = models.ImageField(upload_to='app/')