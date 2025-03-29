from djongo import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    species = models.CharField(max_length=50)
    owner = models.CharField(max_length=100)
    born_date = models.DateField()

