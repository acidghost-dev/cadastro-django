from django.shortcuts import render, redirect
from .models import Usuario
def index(request):
    return render(request, 'usuarios/index.html')


def usuarios(request):
  
    if request.method == 'POST' : 
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.email = request.POST.get('email')
        novo_usuario.save()
        return redirect('usuarios')

    usuarios = Usuario.objects.all()
    
    return render(request, 'usuarios/usuarios.html', {'usuarios': usuarios})
