from rest_framework import serializers
from .models import *

class LogoSerializer(serializers.ModelSerializer):
	class Meta:
		model=Logo
		fields='__all__'

class ObjectifSerializer(serializers.ModelSerializer):
	class Meta:
		model=Objectif
		fields='__all__'

class EquipeSerializer(serializers.ModelSerializer):
	class Meta:
		model=Equipe
		fields='__all__'
