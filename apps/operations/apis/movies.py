# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from rest_framework.viewsets import ModelViewSet

# project imports
from apps.operations.models import Movie
from apps.operations.serializers import MovieSerializer


class MovieViewSet(ModelViewSet):
    model = Movie
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    http_method_names = ['get']