from django.db import models
from django.contrib.auth.models import User


class Collection(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Item(models.Model):
    name = models.CharField(max_length=255)
    item_data = models.JSONField(default=dict, blank=True)
    collection = models.ForeignKey(
        Collection,
        on_delete=models.CASCADE,
        related_name='items'
    )

    def __str__(self):
        return f"{self.name} ({self.collection.name})"

    class Meta:
        ordering = ['name']
