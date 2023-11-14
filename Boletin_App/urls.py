from django.urls import path
from .views import tu_vista

urlpatterns = [
    path('', tu_vista, name='formulario'),
    path('fin/', tu_vista, name='fin'),
]