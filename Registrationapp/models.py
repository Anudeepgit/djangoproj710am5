from django.db import models
class Register(models.Model):
    UserName=models.CharField(max_length=20)
    Password=models.CharField(max_length=20)
    Confirmpassword=models.CharField(max_length=20)
    Mobile=models.IntegerField()
    DOB=models.DateField()

# Create your models here.
