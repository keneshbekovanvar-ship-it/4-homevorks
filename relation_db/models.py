from django.db import models


class TouristCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    categories = models.ManyToManyField(
        TouristCategory,
        related_name='persons'
    )

    def str(self):
        return f"{self.first_name} {self.last_name}"
