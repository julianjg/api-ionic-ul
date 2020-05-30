from rest_framework  import viewsets

from .models import Book, CategoriaNegocio, Panaderia, Supermercado
from .serializer import BookSerializer
from .serializer import CategoriaNegocioSerializer
from .serializer import PanaderiaSerializer
from .serializer import SupermercadoSerializer

class BookViewSets(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CategoriaNegocioViewSets(viewsets.ModelViewSet):
    queryset = CategoriaNegocio.objects.all()
    serializer_class = CategoriaNegocioSerializer

class PanaderiaViewSets(viewsets.ModelViewSet):
    queryset = Panaderia.objects.all()
    serializer_class = PanaderiaSerializer

class SupermercadoViewSets(viewsets.ModelViewSet):
    queryset = Supermercado.objects.all()
    serializer_class = SupermercadoSerializer