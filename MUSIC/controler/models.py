from enum import unique
from pickle import TRUE
from django.db import models
from tinymce.models import HTMLField

class edits(models.Model):
    News_title=models.CharField(max_length=50)
    News_dis=HTMLField()

    
class mod(models.Model):
    mod_title=models.CharField(max_length=50)
    mod_dis=HTMLField()


class trend(models.Model):
    trend_title1=models.CharField(max_length=30)    
    trend_title2=models.CharField(max_length=30)    
    trend_title3=models.CharField(max_length=30)    
    trend_title4=models.CharField(max_length=30)    
    trend_title5=models.CharField(max_length=30)

    
# Create your models here.
