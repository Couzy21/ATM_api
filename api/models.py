# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Agents(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user)
   
class Account(models.Model):
    balance = models.IntegerField(default=0)
    Customer = models.OneToOneField("Customer", on_delete=models.CASCADE)
    agent = models.ForeignKey("Agents", on_delete=models.CASCADE)   
    
    
    
    def __str__(self):
        return str(self.Customer)

      