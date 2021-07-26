from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Puppies_List(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name = 'purchases',null=True)
    name = models.CharField(max_length=200, null= True)
    breed = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    age = models.IntegerField()
    date = models.DateField(null=True)

    def __str__(self):
        return self.name
