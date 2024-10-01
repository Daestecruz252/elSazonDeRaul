from rest_framework import viewsets
from .models import gerente, inventario
from .serializers import gerenteserializers, inventarioserializers

class gerenteViewSet(viewsets.ModelViewSet):
    queryset = gerente.objects.all()
    serializer_class = gerenteserializers

class inventarioViewSet(viewsets.ModelViewSet):
    queryset = inventario.objects.all()
    serializer_class = inventarioserializers
    