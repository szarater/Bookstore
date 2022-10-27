from django.shortcuts import redirect, render
from django.urls import is_valid_path
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
    formulario_contacto=FormularioContacto()
    if request.method=='POST':
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get('nombre')
            email=request.POST.get('email')
            contenido=request.POST.get('contenido')

            email=EmailMessage('Mensaje desde App Django', 
            'El usuario con nombre {} con la direccion {} escribe lo siguiente:\n\n {}'.format(nombre,email,contenido),'',['szarater7@gmail.com'],reply_to=[email])

            try:
                email.send()
                return redirect('/contacto/?valido')
            except:
                return redirect('/contacto/?novalido')

    return render(request, 'contacto/contacto.html', {'miFormulario':formulario_contacto})