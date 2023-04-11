from django.http import HttpResponse
from django.template import Template, Context, loader

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
