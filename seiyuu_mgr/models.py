#!/usr/bin/env python
from django.db import models

# Create your models here.

class Seiyuu(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    page_link = models.URLField(null=True)
    image_link = models.URLField(null=True)

    @property
    def full_name(self):
        return u"%s %s" % (self.first_name, self.last_name)

    def get_role_for_season(self, season):
        return self.character_set.filter(anime__season=season)

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)

class Anime(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.DateField(null=True)
    page_link = models.URLField(null=True)
    image_link = models.URLField(null=True)
    season = models.ForeignKey('Season', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return u"%s" % self.name

class Character(models.Model):
    STATUS = (
        ("MAIN", "Main"),
        ("SUPPORT", "Supporting")
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    seiyuu = models.ManyToManyField('Seiyuu')
    anime = models.ManyToManyField('Anime')
    status = models.CharField(max_length=200, choices=STATUS)
    page_link = models.URLField(null=True)
    image_link = models.URLField(null=True)
    last_modified = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return u"%s %s" % (self.first_name, self.last_name)

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)

class Season(models.Model):
    label = models.CharField(max_length=20)
    starting_date = models.DateField()

    def __str__(self):
        return "%d - %s" % (self.id, self.label)
