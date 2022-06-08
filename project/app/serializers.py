from dataclasses import field
from rest_framework import serializers

from app.models import Alvo, Descargas

class DescargasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descargas
        exclude = []

class AlvoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alvo
        exclude = []