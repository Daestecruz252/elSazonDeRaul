from rest_framework import serializers
from .models import gerente, inventario

class gerenteserializers(serializers.ModelSerializer):
    class Meta:
            model = gerente
            fields = '__all__'
            
class inventarioserializers(serializers.ModelSerializer):
    class Meta:
            model = inventario
            fields = '__all__'