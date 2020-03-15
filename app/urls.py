from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/',views.createReport, name='create_form'), # Para acceder a la url de creación
    url(r'^edit/(?P<id>\d+/)$',views.editReport, name='edit_form'), # Para acceder a la url de editar un registro
    url(r'^delete/(?P<id>\d+/)$',views.deleteReport, name='delete_form'), # Para acceder a la url de eliminar un registro
]