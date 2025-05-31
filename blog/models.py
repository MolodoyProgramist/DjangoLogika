from datetime import timedelta
from django.utils import timezone
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)  # Виправлено CharField
    bio = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField()
    author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

    def published_recently(self):
        return self.published_date >= timezone.now() - timedelta(days=7)


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField()
    author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
