from django.db import models

# Create your models here.
class SaveInfo(models.Model):
    First_Name=models.CharField( max_length=50)
    Last_Name=models.CharField(max_length=50)
    Email=models.CharField(max_length=60)
    Password=models.CharField(max_length=50)
    
    
    
