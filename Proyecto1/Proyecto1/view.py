from pipes import Template
from django.template import loader
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
import datetime

def saludo(request): #primera vista

    documento ='''<html>
    <body>
    <h1>
    Esta es mi primera página web
    </h1>
    </body>
    </html>
    '''
    return HttpResponse (documento)

#Curso Django parte 3

def damefecha(request): #primera vista

    fecha_actual = datetime.datetime.now()
    documento ='''<html>
    <body>
    <h1>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html> ''' %fecha_actual

    return HttpResponse (documento)


#Curso Django parte 4
def calculaEdad(request, year): 
    edadActual= 18
    periodo= year - 2019
    edadFutura = edadActual + periodo
    
    documento ='''<html>
    <body>
    <h2>
    En el año %s tendrás %s años 
    </h2>
    </body>
    </html> ''' %(year, edadFutura)

    return HttpResponse (documento)

#Curso Django parte 5. Plantillas
#La cadena HTML se debe guardar en otro archivo
'''¿Como crear una plantilla?
-Crear un objeto tipo tablate
-Creación de contexto
-Renderización del template
'''
def saludo_plantilla(request): 

    #Declarar variables:  Django parte 6. Plantillas II
    nombre = 'Marcos'
    apellido = 'Díaz'
    fecha_actual = datetime.datetime.now()
    #Curso Django parte 7. Plantillas III
    temas=['Plantillas','Modelos', 'Formularios', 'Vistas', 'Despliegue']
   
    ''' Orden de las llamadas:
    diccionario
    atributo
    método
    indice de lista
    '''
   
    doc_externo = open("C:/Users/RafaelJiménez/Python/proyectoDjango/Proyecto1/Proyecto1/Plantilla/miplantilla.html")
    plt = Template(doc_externo.read())
    doc_externo.close()
    ctx = Context({"nombre_persona":nombre, "apellido_persona":apellido, "momento_actual":fecha_actual, "temas":temas})
    documento = plt.render(ctx)
    
    return HttpResponse (documento)

def saludo_loader(request): 
 #Curso Django parte 8. Plantillas IV
    '''
    Existen multitud de filtros |
    También de flujo de control
    aunque no es muy recomendable
    Cargador de plantillas para que recopile de totas las plantillas
        Tenemos que ir a Settings.py y buscar Templante
            en DIRs añadir direccion
    '''
    nombre = 'Marcos'
    apellido = 'Díaz'
    fecha_actual = datetime.datetime.now()
    #Curso Django parte 7. Plantillas III
    temas=['Plantillas','Modelos', 'Formularios', 'Vistas', 'Despliegue']

    #doc_externo = loader.get_template('miplantilla.html')
    diccionario = {"nombre_persona":nombre, "apellido_persona":apellido, "momento_actual":fecha_actual, "temas":temas}
    #documento = doc_externo.render(diccionario)

#Curso Django parte 9. Método para simplificar el método anterior
# Plantillas V Plantillas incrustadas

    return render(request, 'miplantilla.html', diccionario)

def cursoC(request):

     fecha_actual = datetime.datetime.now()

     return render(request, 'cursoC.html', {"dameFecha":fecha_actual})

def cursoCss(request):
    
     fecha_actual = datetime.datetime.now()

     return render(request, 'cursoCss.html', {"dameFecha":fecha_actual})



