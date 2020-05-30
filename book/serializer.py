from.models import Book, CategoriaNegocio, Panaderia, Supermercado
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class CategoriaNegocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaNegocio
        fields = '__all__'

class PanaderiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panaderia
        fields = '__all__'

class SupermercadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supermercado
        fields = '__all__'