from django.db import models

# Create your models here.
class Employee(models.Model):
    
    identification= models.CharField(max_length=12)
    name = models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    salary=models.IntegerField()
    is_activate= models.BooleanField(default=True)
