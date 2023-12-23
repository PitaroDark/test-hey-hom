from django.db import models

# Create your models here.
class Clients(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Transactions(models.Model):
    TYPE_OPERATION = (
        ('top-up', 'suma'),
        ('deduction', 'resta'),
    )
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    operation = models.CharField(max_length=50, choices=TYPE_OPERATION)
    amont = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def sum():
        pass
    