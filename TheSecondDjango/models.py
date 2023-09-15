from django.db import models


class Clients(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    phone_number = models.IntegerField()
    address = models.CharField(max_length=200)
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.name}'


class Products(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=400)
    price = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateTimeField()
    image = models.ImageField(null=True)

    def __str__(self):
        return f'{self.name}'


class Orders(models.Model):
    name_client = models.ForeignKey(Clients, on_delete=models.CASCADE, null=True)
    name_product = models.ManyToManyField(Products)
    price = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.name_client} - {self.name_product}'
