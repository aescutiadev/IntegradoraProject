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
    event = Eventos.objects.all().order_by('-created')
    estado = Estados.objects.all()
    return render(request, 'eventos/event_list.html' and 'eventos/event_destacados.html', {'event': event, 'estado': estado})


def buscar(request, nombre):
    event = Eventos.objects.filter('name')
    return render(request, 'eventos/event_list.html', {'event': event})


def contacto(request):
	register_form = ContactoForm()
	if (request.method == "POST"):
		register_form = ContactoForm(data=request.POST)
		if(register_form.is_valid()):
			try:         
				nombre = request.POST.get("nombre")
				correo = request.POST.get("correo")
				tel = request.POST.get("tel")
				comentario = request.POST.get("comentario")
				#Se crea una instancia comentario que construira el nuevo registro 
				nuevoComentario = Comentario() 
				#Se asigna como valor del comentario el valor recuperado del formulario 
				nuevoComentario.nombre = nombre
				nuevoComentario.correo = correo
				nuevoComentario.tel = tel           
				nuevoComentario.coment = comentario  
				#Se almacena el nuevo comentrio en la tabla de la base de datos   
				if (nuevoComentario.nombre == "" or nuevoComentario.nombre == None):
					pass
				elif (nuevoComentario.correo == "" or nuevoComentario.correo == None):
					pass
				elif (nuevoComentario.tel == "" or nuevoComentario.tel == None):
					pass    
				else:
					nuevoComentario.save()
					return redirect(reverse('Contacto')+"?ok")
				#Si tido es correcto se redirecciona a la página de comentario y se indica que todo es correcto   Contacto es el nombre de la url             
			except:
				#Si ocurre algun problema se redirecciona a la página de comentario y se indica que algo salio mal  
				return redirect(reverse('Contacto')+"?fail") 
	return render(request,"eventos/contact.html",{'form':register_form})
    #return render(request, 'eventos/contact.html', locals())


def details(request, id):
    evento = get_object_or_404(Eventos, id=id)
    return render(request, 'eventos/event_detail.html', {'evento': evento})
