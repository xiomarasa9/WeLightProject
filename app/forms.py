from django import forms
from app.models import MonitoringReports


class ReportForm(forms.ModelForm):
    class Meta:
        model = MonitoringReports
        fields = ['date','energy','reactive_energy','power','maximeter','reactive_power','voltage','intensity','power_factor',]
        