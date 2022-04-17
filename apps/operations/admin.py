# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from django.contrib import admin

# model imports
from apps.operations.models import *

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):

    list_filter = (
        "title",
        "description",
        "release_date",
        "no_of_actors",
        "vote_count",
    )
    list_display = (
        "title",
        "description",
        "release_date",
        "no_of_actors",
        "vote_count",
    )
    search_fields = (
        "title",
        "description",
        "release_date",
        "no_of_actors",
        "vote_count",
    )
    
@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):

    list_filter = (
        "name",
        "birth_date",
        "no_of_movies",
    )
    list_display = (
        "name",
        "birth_date",
        "no_of_movies",
    )
    search_fields = (
        "name",
        "birth_date",
        "no_of_movies",
    )

@admin.register(Connector)
class ConnectorAdmin(admin.ModelAdmin):
    
    list_filter = (
        "movie",
        "actor",
    )
    list_display = (
        "movie",
        "actor",
    )
    search_fields = (
        "movie",
        "actor",
    )