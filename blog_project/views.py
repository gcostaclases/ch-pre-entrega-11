from django.shortcuts import render


# Esta vista pertenece al proyecto general porque muestra la página de inicio.
def inicio(request):
    return render(request, "project/inicio.html")


# Esta vista pertenece al proyecto general porque presenta información del sitio.
def acerca(request):
    return render(request, "project/acerca.html")
