# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# project imports
from utils.core.models import TimeStampable

"""
Crated table to store actor details
"""
class Actor(TimeStampable):
    
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=255
    )
    
    birth_date = models.DateField(
        verbose_name=_("Date Of Birth")
    )
    
    no_of_movies = models.IntegerField(
        verbose_name = _("No Of Movies"),
        default = 0,
        editable = False
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Actor")
        verbose_name_plural = _("Actors")
        unique_together = ("name", "birth_date")
        indexes = [models.Index(fields=[
            "id", 
            "no_of_movies"
        ])]