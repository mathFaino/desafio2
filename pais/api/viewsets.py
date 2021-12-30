from rest_framework.viewsets import ModelViewSet
from pais.models import Pais
from pais.api.serializers import PaisSerializerList


class PaisViewSet(ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializerList
