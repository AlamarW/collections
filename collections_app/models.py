from django.contrib.auth.models import User
from django.db import models


class Collection(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    collection_items = models.ManyToManyField(
        "Item", related_name="collections", blank=True
    )
    collection_schema = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Item(models.Model):
    name = models.CharField(max_length=255)
    item_data = models.JSONField(default=dict, blank=True)
    item_collection = models.ForeignKey(
        Collection, on_delete=models.CASCADE, related_name="items"
    )

    def __str__(self):
        return f"{self.name} ({self.collection.name})"

    class Meta:
        ordering = ["name"]
