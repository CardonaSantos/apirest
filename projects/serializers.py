#nos permite llamar un modulo especial de rest framework

from rest_framework import serializers
from .models import Project #una vez le decimos esto va a sabera a que nos referimos cuando se haga una peticion post, get etc.

#convierte un modelo en datos que podrán ser consultados.
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project #abajo los campos que podrán ser consultados
        fields = ('id', 'title', 'description', 'tecnology', 'create_at')
        read_only_fields = ('create_at',)#que campos solo son de lectura


