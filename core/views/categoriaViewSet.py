from core.serializers import CategoriaSerializer
from rest_framework.viewsets import ModelViewSet

from core.models import Categoria


class CategoriaViewset(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
