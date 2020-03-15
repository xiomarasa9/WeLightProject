from __future__ import unicode_literals

from django.db import models

# Se ha creado el modelo según el csv
class MonitoringReports(models.Model):
    
    # Atributos del modelo
    id = models.AutoField(primary_key = True)
    date = models.CharField(max_length=100)
    energy = models.FloatField(max_length=20)
    reactive_energy = models.FloatField(max_length=20)
    power = models.FloatField(max_length=20)
    maximeter = models.FloatField(max_length=20)
    reactive_power = models.FloatField(max_length=20)
    voltage = models.FloatField(max_length=20)
    intensity = models.FloatField(max_length=20)
    power_factor = models.FloatField(max_length=20)
