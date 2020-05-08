from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from app.models import MonitoringReports
from app.forms import ReportForm

# Se muestra la información de la tabla completa en la vista principal.
def index(request):
    # Obtener todo el objeto
    read = MonitoringReports.objects.all()
    return render(request, 'index.html', {'read_data': read})


# Crea un registro nuevo
def createReport(request):
    if request.method == 'POST':
        create_form = ReportForm(request.POST)
        if create_form.is_valid(): # Se va todo bien
            create_form.save()
            return redirect('index') # redigirir a la página principal
    else:
        create_form = ReportForm()
    return render(request, 'create_form.html', {'create_form': create_form})


# Sobre un registro ya creado, elimina los valores deseados
def editReport(request, id):
    report = MonitoringReports.objects.get(id = id)
    if request.method == 'GET':
        edit_form = ReportForm(instance = report)
    else:
        edit_form = ReportForm(request.POST, instance = report)
        if edit_form.is_valid():
            edit_form.save()
        return redirect('index')  # redigirir a la página principal
    return render(request, 'edit_form.html', {'edit_form': report})


# Elimina un registro
def deleteReport(request,id):
    report = MonitoringReports.objects.get(id = id)
    if request.method == 'POST':
        report.delete()
        return redirect('index')  # redigirir a la página principal
    return render(request,'delete_form.html', {'delete_form': report})