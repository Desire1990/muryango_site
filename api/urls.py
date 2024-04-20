from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register('logo', LogoViewSet)
router.register('objectif', ObjectifViewSet)
router.register('equipe', EquipeViewSet)



urlpatterns=[
	path('',include(router.urls)),
	path('api_auth', include('rest_framework.urls'))
]