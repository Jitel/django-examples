from django.db import models


class Articlres(models.Model):
    title = models.CharField(max_length=200)
    post = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title