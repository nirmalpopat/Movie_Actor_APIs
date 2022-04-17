# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# model imports
from .actors import Actor
from .movies import Movie

# project imports
from utils.core.models import TimeStampable

"""
Create below model to connect actor and movie
"""
class Connector(TimeStampable):
    
    movie = models.ForeignKey(
        verbose_name = _("Movie"),
        to = Movie,
        on_delete = models.CASCADE
    )
    
    actor = models.ForeignKey(
        verbose_name = _("Actor"),
        to = Actor,
        on_delete = models.CASCADE
    )
    
    def __str__(self):
        return f'{self.movie.title} created by {self.actor.name}'
    
    class Meta:
        verbose_name = _("Connector")
        verbose_name_plural = _("Connectors")
        unique_together = ("movie", "actor")
        indexes = [models.Index(fields=[
            "id", 
            "movie",
            "actor"
        ])]