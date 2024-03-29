# Django
from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    calories = models.IntegerField(default=0)


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Ingredient, related_name="notes", verbose_name="Теги")
