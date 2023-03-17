from django.db import models
from django.utils import timezone
from django.conf import settings


class Category(models.Model):
    title = models.CharField(max_length=50, primary_key=True)
    status = models.BooleanField(default=True)


class Article(models.Model):
    STATUS_CHOICES = (
        ("d", "draft"),
        ("p", "publish")
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True)
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=1,
                              choices=STATUS_CHOICES,
                              default="d")
