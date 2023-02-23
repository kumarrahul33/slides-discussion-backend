from django.db import models

# Create your models here.
class SlideQue(models.Model):
    SlideId = models.CharField(max_length=10)
    PageNo = models.IntegerField()
    Question = models.CharField(max_length=100)
    Answer = models.CharField(max_length=500)