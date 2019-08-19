from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	path('', views.principal, name='Principal'),
	path('evento/<int:id>/', views.details, name='Detalles'),
	path('contacto/', views.contacto, name='Contacto'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)