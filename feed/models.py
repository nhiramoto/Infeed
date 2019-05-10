from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class List(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Source(models.Model):
    source_list = models.ForeignKey(List, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    item_source = models.ForeignKey(Source, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    url = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    summary = models.TextField()
    readed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
