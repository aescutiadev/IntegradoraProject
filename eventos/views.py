from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Eventos, Estados, Comentario
from .forms import ContactoForm
from django.urls import reverse

# Create your views here.


def principal(request):
    query = request.GET.get('q', '')
    if query == "":
        event = Eventos.objects.all()
    else:
        event = Eventos.objects.filter(name__contains=query)
		
    estado = Estados.objects.all()
    return render(request, 'eventos/event_list.html' and 'eventos/event_destacados.html', {'event': event, 'estado': estado})

def buscar_estado(request, estado):
	# Obtiene el nombre del formulario Estados y lo asigna a una variable
	obj_estado = Estados.objects.get(nombre=estado)
	# Obtiene los datos de los Eventos en la base de datos y se filtrarán respecto al valor asignado en la variable
	event = Eventos.objects.all().filter(estado=obj_estado)
	# Obtiene la lista de los estados registrados
	estado = Estados.objects.all()
	return render(request, 'eventos/event_list.html', {'event': event, 'estado': estado})

def contacto(request):
	register_form = ContactoForm()
	if (request.method == "POST"): # Si hay un método POST en un formulario...
		register_form = ContactoForm(data=request.POST)
		if(register_form.is_valid()):
			try:         
				nombre = request.POST.get("nombre","")
				correo = request.POST.get("correo","")
				tel = request.POST.get("tel","")
				comentario = request.POST.get("comentario","")
				# Validamos que los campos estén vacios
				if nombre != "" and correo !="" and tel != "" and comentario != "":
					#Se crea una instancia comentario que construira el nuevo registro 
					nuevoComentario = Comentario() 
					#Se asignan los campos los valores recuperados del formulario 
					nuevoComentario.nombre = nombre
					nuevoComentario.correo = correo
					nuevoComentario.tel = tel           
					nuevoComentario.coment = comentario  
					#Se almacena el nuevo comentrio en la tabla de la base de datos   
					nuevoComentario.save()
					#Si tido es correcto se redirecciona a la página de comentario y se indica que todo es correcto   Contacto es el nombre de la url 
					messages.success(request, 'Su mensaje se envio') 
					return redirect("/contacto/")
				else:
					messages.error(request, 'Todos los campos deben de ser llenados')
					return redirect("/contacto/")           
			except:
				#Si ocurre algun problema se redirecciona a la página de comentario y se indica que algo salio mal  
				messages.error(request, 'Ocurrio un erro, intente mas tarde')
				return redirect("/contacto/") 

	return render(request,"eventos/contact.html",{'form':register_form})


def details(request, id):
    evento = get_object_or_404(Eventos, id=id)
    return render(request, 'eventos/event_detail.html', {'evento': evento})
