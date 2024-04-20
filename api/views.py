
from rest_framework import viewsets
from .models import *
from .serializers import *


class LogoViewSet(viewsets.ModelViewSet):
	queryset = Logo.objects.all()
	serializer_class = LogoSerializer


class ObjectifViewSet(viewsets.ModelViewSet):
	queryset = Objectif.objects.all()
	serializer_class = ObjectifSerializer


class EquipeViewSet(viewsets.ModelViewSet):
	queryset = Equipe.objects.all()
	serializer_class = EquipeSerializer
