from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import FormularioContacto

# Create your views here.

def busqueda_productos(request):

    return render(request, "busqueda_productos.html")

def buscar(request):

    if request.GET['producto']:

        #mensaje = "Árticulo buscado: %r" %request.GET['producto']
        product = request.GET['producto']

        if len(product)>20:

            mensaje = 'Texto de búsqueda demasiado largo'
        else:

            #incontrains funciona a un like de sql
            articulos = Articulos.objects.filter(nombre__contains=product)
            return render(request, "resultados_busqueda.html", {"articulos":articulos, "query": product})
    
    else:

        mensaje = 'No has introducido nada'

    return HttpResponse(mensaje)

    #formulario de contactos

''' Clase anterior
def contacto(request):

    if request.method == 'POST':

        subject = request.POST['asunto']

        message = request.POST['mensaje'] + ' ' + request.POST['email']

        email_from = settings.EMAIL_HOST_USER

        recipient_list = ['rafa_carrizal@hotmail.com']

        send_mail (subject, message, email_from, recipient_list)

        return render(request, 'gracias.html')

    return render(request, 'contacto.html')
    '''

def contacto(request):

    if request.method == 'POST':

        miFormulario = FormularioContacto(request.POST)

        if miFormulario.is_valid():
                infform =miFormulario.cleaned_data

                send_mail(infform['asunto'], infform['mensaje'],
                infform.get('email', ''), ['rafa_carrizal@hotmail.com'], )

                return render(request, 'gracias.html')

    else:

        miFormulario = FormularioContacto()
    
    return render(request, 'formulario_contacto.html', {'form': miFormulario})


