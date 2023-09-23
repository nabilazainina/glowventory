from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    category = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)