from django.http import HttpResponse
from django.template import Template, Context, loader
from .models import *


def saludar(request):
    return HttpResponse("!hola mundo!")


#def probandoHtml(request):

   # diccionario={"nombre":"Nacho", "apellido": "Suarez", "edad":25}

    # archivo=open(r"C:\Users\isuarez\python2\Tercera pre-entrega Suarez\Terceratp\Plantillas\template1.html")

    # template=Template(archivo.read())
    # archivo.close()
    
    # contexto=Context(diccionario)
    # documento=template.render(contexto)
      

   # return HttpResponse(documento)


def probandoHtml(request):  

    diccionario={"nombre":"Nacho", "apellido": "Suarez", "edad":25}

    template=loader.get_template("template1.html")

    documento=template.render(diccionario)

    return HttpResponse(documento)


def cargar_libro(request):
    
    titulo_libro="La Metamorfosis"
    nombre_editorial="Kurt Wolff Verlag"
    cantidad_paginas=80

    libro=Libro(titulo=titulo_libro, editorial=nombre_editorial, paginas=cantidad_paginas)
    libro.save()

    respuesta=f"se a cargado el libro: {titulo_libro}"

    return HttpResponse(respuesta)