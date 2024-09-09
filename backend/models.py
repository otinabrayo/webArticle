from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(max_length=200)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
