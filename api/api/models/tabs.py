from django.db import models
from django.contrib.auth.models import User

from models.links import Link
from models.tags import Tag


class Tab(models.Model):
    user = models.ForeignKey(User)
    link = models.ForeignKey(Link)
    tag = models.ForeignKey(Tag)
    publicated_date = models.DateField(blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)

