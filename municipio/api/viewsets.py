from rest_framework.viewsets import ModelViewSet
from municipio.models import Municipio
from .serializers import MunicipioSerializer


class MunicipioViewSet(ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer

