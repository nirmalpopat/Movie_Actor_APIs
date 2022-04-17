# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# project imports
from utils.core.models import TimeStampable

"""
Crated table to store movie details
"""
class Movie(TimeStampable):
    
    title = models.CharField(
        verbose_name=_("Title"),
        max_length=255,
        unique = True
    )
    
    description = models.TextField(
        verbose_name=_("Description")
    )
    
    release_date = models.DateField(
        verbose_name=_("Release Date")
    )
    
    no_of_actors = models.IntegerField(
        verbose_name = _("No Of Actors"),
        default = 0,
        editable = False
    )
    
    vote_count = models.IntegerField(
        verbose_name = _("Vote Count"),
        default = 0,
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("Movie")
        verbose_name_plural = _("Movies")
        indexes = [models.Index(fields=[
            "id",  
            "no_of_actors", 
            "vote_count"
        ])]