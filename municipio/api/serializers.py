from rest_framework.serializers import ModelSerializer
from municipio.models import Municipio
from estado.api.serializers import EstadoSerializer


class MunicipioSerializer(ModelSerializer):
    estado = EstadoSerializer()

    class Meta:
        model = Municipio
        fields = (
            'id', 'nome', 'populacao', 'estado')
