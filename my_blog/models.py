from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=225, null=False, blank=False)
    author = models.CharField(max_length=225, null=False, blank=False)
    author_key = models.ForeignKey(User, blank=True, null=True)
    content = models.TextField(null=False, blank=False)


class Comment(models.Model):
    comment = models.CharField(max_length=225)
    article = models.ForeignKey(Article, null=True)
