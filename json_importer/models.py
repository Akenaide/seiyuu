#!/usr/bin/env python
from django.db import models

class JsonFile(models.Model):
    label = models.CharField(max_length=30, null=True, blank=True)
    json_file = models.FileField(upload_to='json_file')

    def __unicode__(self):
        return unicode(self.label)
