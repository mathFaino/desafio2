from rest_framework.serializers import ModelSerializer
from pais.models import Pais


class PaisSerializerList(ModelSerializer):

    class Meta:
        model = Pais
        fields = (
            'id', 'nome', 'sigla')

