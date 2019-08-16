from django.db import models

# Create your models here.
class Eventos(models.Model):
	"""Model definition for Eventos."""
	# TODO: Define fields here
	name = models.CharField(max_length=50,verbose_name="Nombre")
	estado = models.ForeignKey('Estados', on_delete=models.CASCADE, blank=True, null=True, verbose_name="Estado")
	city = models.CharField(max_length=50,verbose_name="Ciudad")
	descripcion = models.TextField(verbose_name="Descripción")
	date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Fecha del Evento")
	hora = models.TimeField(auto_now=False, auto_now_add=False, verbose_name="Hora del Evento")
	km = models.CharField( max_length=12, verbose_name="Kilómetros de recorrido",blank=True,null=True)
	time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name="Tiempo de recorrido")
	punto_inicio = models.CharField(max_length=50,verbose_name="Punto de inicio",blank=True,null=True)
	costo = models.FloatField(verbose_name="Costo")
	imagen = models.ImageField(upload_to='evento', height_field=None, width_field=None, max_length=None)
	created = models.DateTimeField(auto_now_add=True,verbose_name="Creación") # Fecha y tiempo
	updated = models.DateTimeField(auto_now_add=True,verbose_name="Modificado")

	class Meta:
		"""Meta definition for Eventos."""

		verbose_name = 'Evento'
		verbose_name_plural = 'Eventos'
		ordering = ["-created"]

	def __str__(self):
		"""Unicode representation of Eventos."""
		return self.name

class Estados(models.Model):
	"""Model definition for Estados."""
	# TODO: Define fields here
	nombre = models.CharField(max_length=50, verbose_name="Estado")
	image = models.ImageField(upload_to='estado', height_field=None, width_field=None, max_length=None)
	class Meta:
		"""Meta definition for Estados."""
		verbose_name = 'Estado'
		verbose_name_plural = 'Estados'
		ordering = ["nombre"]

	def __str__(self):
		"""Unicode representation of Estados."""
		return self.nombre
