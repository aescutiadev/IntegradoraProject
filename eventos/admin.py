from django.contrib import admin
from .models import Eventos,Estados

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
	readonly_fields = ('created','updated') # Los datos de creación y modificación son sólo lectura

admin.site.register(Eventos, AdministrarModelo)
admin.site.register(Estados)