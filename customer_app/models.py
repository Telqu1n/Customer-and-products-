from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    
    def __str__(self):
        return self.full_name()


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    
    def __str__(self):
        return f'{self.name}, {self.price}'