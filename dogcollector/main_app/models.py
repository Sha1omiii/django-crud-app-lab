from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField()
    age = models.IntegerField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name

class Toy(models.Model):
    name = models.CharField(max_length=100)
    dogs = models.ManyToManyField(Dog)

    def __str__(self):
        return self.name
