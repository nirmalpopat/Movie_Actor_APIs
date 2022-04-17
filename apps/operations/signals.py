# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import F

# local import
from apps.operations.models import *

# i want to store records when i update stock

@receiver(post_save, sender=Connector)
def fun(sender, instance, created, **kwargs):
    if created:
        instance.movie.no_of_actors = F('no_of_actors') + 1
        instance.actor.no_of_movies = F('no_of_movies') + 1
        instance.movie.save()
        instance.actor.save()