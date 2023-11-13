from django import forms
import datetime
import re
from django.core.exceptions import ValidationError

class Formulario(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    fechaInicio = forms.DateField(initial=datetime.date.today, widget = forms.HiddenInput(), required = False)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        fechaInicio = cleaned_data.get('fechaInicio')

        if username == password:
            raise ValidationError('El usuario y contraseña no deben coincidir')

        if username.lower() in password.lower():
            raise ValidationError('La contraseña no debe incluir el usuario')

        if len(password) < 8:
            raise ValidationError('La longitud de la contraseña debe ser al menos de 8 caracteres')

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError('La contraseña debe incluir al menos un caracter especial [!¡@_?¿=_-]')

        if not re.search(r'\d', password):
            raise ValidationError('La contraseña debe incluir al menos un número')

        if not re.search(r'[A-Z]', password):
            raise ValidationError('La contraseña debe incluir al menos un caracter en mayúsculas')

        if not re.search(r'[a-z]', password):
            raise ValidationError('La contraseña debe incluir al menos un caracter en minúsculas')

        return cleaned_data