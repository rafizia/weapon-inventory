from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    atk = models.IntegerField()
    rarity = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.IntegerField()
