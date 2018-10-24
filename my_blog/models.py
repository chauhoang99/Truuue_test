from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=225, null=False, blank=False)
    author = models.CharField(max_length=225, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
