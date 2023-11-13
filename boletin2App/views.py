from django.shortcuts import render
from .forms import Formulario

def welcome(request):
    return render(request, 'boletin2App/index.html', {})

def hacerFormulario(request):
    enviado = None

    if request.method == 'POST':
        form = Formulario(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            fechaInicio = form.cleaned_data['fechaInicio']

            enviado = True
    else:
        form = Formulario()

    return render(request, 'boletin2App/hacerFormulario.html', {'form': form, 'enviado': enviado})
