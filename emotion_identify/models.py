from django.db import models

# Create your models here.
class UploadVoice(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length = 600,default='NA')
    emotion = models.CharField(max_length=100,default='NA')
    audio = models.FileField(upload_to='speech/')

class Sample(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length = 600,default='NA')
    emotion = models.CharField(max_length=100,default='NA')
    audio = models.FileField(upload_to='sample/')
