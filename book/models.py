from django.db import models

class Book(models.Model):
    # поля с урока
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    pages = models.IntegerField()
    price = models.FloatField()
    published_date = models.DateField()

    # самостоятельное изучение (TODO)
    cover = models.FileField(upload_to='books/', null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    # дополнительные поля
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title
