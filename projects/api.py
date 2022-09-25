from.models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset=Project.objects.all()  #que consultas se van a poder hacer
    permission_classes= [
        permissions.AllowAny
    ]
    #decimos que cualquiera puede acceder a la api, despues podemos modificar para que pida autenticacion
    serializer_class= ProjectSerializer
    