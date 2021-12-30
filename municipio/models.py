from django.db import models
from estado.models import Estado


class Municipio(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    nome = models.CharField(max_length=200, null=False, blank=False)
    populacao = models.CharField(max_length=9, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)
