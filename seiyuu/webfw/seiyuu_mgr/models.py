from django.db import models

# Create your models here.

class Seiyuu(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    page_link = models.URLField()
    image_link = models.URLField()

class Anime(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.DateField()
    page_link = models.URLField()
    image_link = models.URLField()

class Character(models.Model):
    STATUS = (
        ("MAIN", "main"),
        ("SUPPORT", "support")
    )
    seiyuu = models.ForeignKey('Seiyuu')
    anime = models.ForeignKey('Anime')
    season = models.CharField(max_length=200)
    status = models.CharField(max_length=200, choices=STATUS)
    page_link = models.URLField()
    image_link = models.URLField()
    last_modified = models.DateTimeField(auto_now=True, auto_now_add=True)