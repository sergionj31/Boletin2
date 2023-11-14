from django.shortcuts import render
from .forms import TuFormulario
from django.utils import timezone

def tu_vista(request):
    if request.method == 'POST':
        form = TuFormulario(request.POST)
        if form.is_valid():
            # Realizar acciones con los datos si es necesario
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            timestamp = form.cleaned_data['timestamp']

            # Redirigir a una página de éxito o realizar cualquier otra acción
            return render(request, 'final.html', {'username': username, 'timestamp': timestamp})
    else:
        form = TuFormulario(initial={'timestamp': timezone.now()})

    return render(request, 'tu_template.html', {'form': form})
