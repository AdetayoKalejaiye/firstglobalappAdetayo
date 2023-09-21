from os import name
from django.db import models

# Create your models here.
class Document(models.Model):
    name = models.CharField(max_length=256)
    file = models.FileField(upload_to='documentation/docs')
    image = models.ImageField(upload_to = 'documentation/images')
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name