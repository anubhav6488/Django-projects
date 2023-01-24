from distutils.command.upload import upload
from typing import Text
from django.db import models

class products(models.Model):
    products_NAME=models.CharField(max_length=50)
    category_NAME=models.CharField(max_length=50)
    Subcategory=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    dis=models.CharField(max_length=50)
    dis=models.CharField(max_length=50)
    publish_date=models.DateField(auto_now_add=False, auto_now=False, blank=True)
    publish_image=models.FileField(upload_to="products/",max_length=250,null=True,default=None)