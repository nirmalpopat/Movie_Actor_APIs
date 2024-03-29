# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from rest_framework import serializers

# project imports
from apps.operations.models import Connector


class ConnectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connector
        fields = [
            "movie",
            "actor",
        ]