# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from rest_framework.viewsets import ModelViewSet

# project imports
from apps.operations.models import Actor
from apps.operations.serializers import ActorSerializer


class ActorViewSet(ModelViewSet):
    model = Actor
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()
    http_method_names = ['get']