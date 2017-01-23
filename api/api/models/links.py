from django.db import models


class Link(models.Model):
    path = models.URLField(max_length=250)
