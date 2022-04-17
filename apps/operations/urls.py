# -*- coding: utf-8 -*-
# python imports
from __future__ import unicode_literals

# lib imports
from rest_framework import routers

# project imports
from apps.operations.apis import *

router = routers.SimpleRouter()

router.register("movies", MovieViewSet, basename="movies")
router.register("actors", ActorViewSet, basename="actors")

urlpatterns = router.urls