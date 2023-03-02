from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

#def buscar(request):
    if request.GET['camada']:
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains = camada)
        return render(request, 'AppCoder/inicio.html', {'cursos': cursos, 'camada': camada})

    else: 
        respuesta = 'ERROR CAMPO SIN RELLENO'

    return render(request, 'AppCoder/inicio.html', {"respuesta": respuesta})

def iniciosesion(request):
    return render(request, 'AppCoder/iniciosesion.html')

def registro(request):
    return render(request, 'AppCoder/registro.html')