from django.contrib import admin
from .models import Eventos,Estados,Comentario

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
	readonly_fields = ('created','updated') # Los datos de creación y modificación son sólo lectura
	list_display = ('name', 'estado','city','date', 'hora', 'time','costo') # Daremos formato a la tabla de alumnos separando en columnas
	search_fields = ('name', 'date', 'hora', 'time','costo') # Agregamos un formulario de busqueda
	date_hierarchy = 'created' # Agregamos busqueda por fecha
	list_filter = ('estado','city','date') # Agregamos filtro lateral
admin.site.register(Eventos, AdministrarModelo)

class AdministrarEstado(admin.ModelAdmin):
	readonly_fields = ('created','updated') # Los datos de creación y modificación son sólo lectura
	list_display = ('nombre','image') # Daremos formato a la tabla de alumnos separando en columnas
	date_hierarchy = 'created' # Agregamos busqueda por fecha
admin.site.register(Estados, AdministrarEstado)

class AdministrarComentarios(admin.ModelAdmin):
	list_display = ('id','nombre','correo','tel','coment') # Daremos formato a la tabla de alumnos separando en columnas
	search_fields = ('id','nombre','correo','tel','created') # Agregamos un formulario de busqueda
	date_hierarchy = 'created' # Agregamos busqueda por fecha
	list_filter = ('created', 'id') # Agregamos filtro lateral

admin.site.register(Comentario, AdministrarComentarios)