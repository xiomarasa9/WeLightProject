from django.contrib import admin
from .models import MonitoringReports

# Se añade el modelo a la url admin.
admin.site.register(MonitoringReports)
