from django.db import models


# create models with fields and parameters
class Dog(models.Model):
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    gender = models.CharField(max_length=200, default='')


class Account(models.Model):
    username = models.CharField(max_length=200)
    realName = models.CharField(max_length=200)
    accountNumber = models.IntegerField()
    balance = models.DecimalField(max_digits=5, decimal_places=2)
