from rest_framework.viewsets import ModelViewSet
from core.models import Autor
from core.serializers import AutorSerializer

class AutorViewset(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer