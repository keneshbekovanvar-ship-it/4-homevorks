from django.db import models

class Book(models.Model):

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    pages = models.IntegerField()
    price = models.FloatField()
    published_date = models.DateField()

    cover = models.FileField(upload_to='books/', null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
