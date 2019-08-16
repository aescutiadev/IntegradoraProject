from django.shortcuts import render
from .models import Eventos,Estados

# Create your views here.
def principal(request):
	event = Eventos.objects.all().order_by('-created')
	return render(request,'eventos/event_list.html' and 'eventos/event_destacados.html', {'event' : event})