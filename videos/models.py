# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=256)
    length = models.PositiveIntegerField()
    release_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    

class Customer(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    phone = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    