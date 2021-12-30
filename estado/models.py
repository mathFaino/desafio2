from django.db import models


class Estado(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    nome = models.CharField(max_length=200, null=False, blank=False)
    sigla = models.CharField(max_length=2, null=False, blank=False)

    def __str__(self):
        return str(self.pk)
