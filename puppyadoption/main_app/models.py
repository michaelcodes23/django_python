from django.db import models
from datetime import datetime
from django.urls import reverse
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Puppies_List(models.Model):
    name = models.CharField(max_length=200, null= True)
    breed = models.TextField()
    description = models.TextField()
    age = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name = 'purchases',null=True)
    price = models.IntegerField()
    date = models.DateField(null=datetime.now)

    def __str__(self):
        return self.name
    #Adding django recommended get_absolute_url method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'puppy_id': self.id})
