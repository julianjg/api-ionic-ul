from rest_framework import routers

from .viewsets import BookViewSets  
from .viewsets import CategoriaNegocioViewSets
from .viewsets import PanaderiaViewSets  
from .viewsets import SupermercadoViewSets

rourter = routers.SimpleRouter()
rourter.register('books', BookViewSets)
rourter.register('categoriasNegocios', CategoriaNegocioViewSets)
rourter.register('panaderias', PanaderiaViewSets)
rourter.register('supermercados', SupermercadoViewSets)

urlpatterns = rourter.urls  