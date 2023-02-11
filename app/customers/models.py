from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=35)
    age = models.PositiveSmallIntegerField(max_length=3)
    city = models.CharField(max_length=20)
    create = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=40)
    business = models.BooleanField()
