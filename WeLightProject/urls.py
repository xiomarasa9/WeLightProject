from django.conf.urls import url, include
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'), # url principal
    url(r'^admin/', admin.site.urls),      # url admin
    url(r'^app/', include('app.urls')),    # apunta a las urls de la app
]
