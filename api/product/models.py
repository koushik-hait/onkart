from django.db import models
from api.catagory.models import Catagory


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    price = models.CharField(max_length=50)
    stock = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    catagory = models.ForeignKey(Catagory, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
