from django.db import models


class SourceList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Source(models.Model):
    source_list = models.ForeignKey(SourceList, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class SourceItem(models.Model):
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    url = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    summary = models.TextField()
    readed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
