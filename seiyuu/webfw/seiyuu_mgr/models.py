from django.db import models

# Create your models here.

class Seiyuu(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    page_link = models.URLField(null=True)
    image_link = models.URLField(null=True)

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)

class Anime(models.Model):
    name = models.CharField(max_length=255)
    start_time = models.DateField()
    page_link = models.URLField(null=True)
    image_link = models.URLField(null=True)
    season = models.ForeignKey('Season', null=True)

    def __unicode__(self):
        return u"%s" % self.name

class Character(models.Model):
    STATUS = (
        ("MAIN", "main"),
        ("SUPPORT", "support")
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    seiyuu = models.ManyToManyField('Seiyuu', null=True)
    anime = models.ManyToManyField('Anime')
    status = models.CharField(max_length=200, choices=STATUS)
    page_link = models.URLField(null=True)
    image_link = models.URLField(null=True)
    last_modified = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)

class Season(models.Model):
    label = models.CharField(max_length=20)

    def __unicode__(self):
        return u"%s" % self.label
