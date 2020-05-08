from django.conf.urls import url
from app import views

app_name = "listado_app"

urlpatterns = [
    url(r'^$', views.index, name='read_data'),
    url(r'^create/$',views.createReport, name='create_form'), # Para acceder a la url de creación
    url(r'^edit/(\d{1,10})/$',views.editReport, name='edit_form'), # Para acceder a la url de editar un registro
    url(r'^delete/(\d{1,10})/$',views.deleteReport, name='delete_form'), # Para acceder a la url de eliminar un registro
]