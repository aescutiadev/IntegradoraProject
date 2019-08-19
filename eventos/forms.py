from django import forms
from .models import Comentario
class ContactoForm(forms.Form):
	class Meta:
		model = Comentario
		fields=('nombre','correo','tel','coment')