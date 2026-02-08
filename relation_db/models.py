from django.db import models


class TouristCategory(models.Model):
    name = models.CharField(max_length=50)

    def str(self):
        return self.name



class Tour(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()

    def str(self):
        return self.title


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    tour = models.OneToOneField(
        Tour,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    categories = models.ManyToManyField(TouristCategory)

    def str(self):
        return f"{self.first_name} {self.last_name}"




class Review(models.Model):
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"Отзыв о {self.person.first_name}"
