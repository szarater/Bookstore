from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='Home'),
    
    path('tienda', views.tienda, name='Tienda'),
]
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)