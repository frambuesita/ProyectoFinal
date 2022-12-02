from django.shortcuts import render
from django.http import HttpResponse

from AppFinal.models import Post,Autor,Estilo
from AppFinal.forms import PostFormulario,AutorFormulario,EstiloFormulario

from django.core import serializers

# Create your views here.

def inicio(request):
    return render(request, 'AppFinal/inicio.html')

def posts(request):
    if request.method == "POST":
            FormularioP = PostFormulario(request.POST)
            print(FormularioP)
 
            if FormularioP.is_valid:
                  informacion = FormularioP.cleaned_data
                  post = Post(post=informacion["post"], fecha_de_creacion=informacion["fecha_de_creacion"])
                  post.save()
                  return render(request, "AppFinal/inicio.html")
    else:
        FormularioP = PostFormulario()
 
    return render(request, "AppFinal/posts.html", {"FormularioP": FormularioP})

def autores(request):
    if request.method == "POST":
            FormularioA = AutorFormulario(request.POST)
            print(FormularioA)
 
            if FormularioA.is_valid:
                  informacion = FormularioA.cleaned_data
                  autor = Autor(nombre=informacion["nombre"], apellido=informacion["apellido"])
                  autor.save()
                  return render(request, "AppFinal/inicio.html")
    else:
        FormularioA = AutorFormulario()
 
    return render(request, "AppFinal/autores.html", {"FormularioA": FormularioA})

def estilos(request):
    if request.method == "POST":
            FormularioE = EstiloFormulario(request.POST)
            print(FormularioE)

            if FormularioE.is_valid:
                informacion = FormularioE.cleaned_data
                estilo = Estilo(estilo=informacion['estilo'])
                estilo.save()
                return render(request, "AppFinal/inicio.html")
    else:
        FormularioE= EstiloFormulario()

    return render(request, "AppFinal/estilos.html", {"FormularioE": FormularioE})



def postsapi(request):
    posts_todos = Post.objects.all()
    return HttpResponse(serializers.serialize('json',posts_todos))

def Autoresapi(request):
    autores_todos = Autor.objects.all()
    return HttpResponse(serializers.serialize('json',autores_todos))

def Estilossapi(request):
    estilos_todos = Estilo.objects.all()
    return HttpResponse(serializers.serialize('json',estilos_todos))

def buscar(request):
    nombre_views=request.GET['nombre']
    autores_todos=Autor.objects.filter(nombre=nombre_views)
    return render(request, "AppFinal/resultadoAutor.html", {'nombre':nombre_views,'autores':autores_todos})

def buscarautor(request):
    return render(request, "AppFinal/busquedaAutor.html")
