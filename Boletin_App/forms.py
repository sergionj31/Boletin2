from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
import re

class TuFormulario(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    timestamp = forms.DateTimeField(widget=forms.HiddenInput, required=False)

    def clean_password(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username == password:
            raise ValidationError("El nombre de usuario y la contraseña no pueden ser iguales.")

        if username.lower() in password.lower():
            raise ValidationError("La contraseña no puede contener el nombre de usuario.")

        if password:
            if len(password) < 8:
                raise ValidationError("La contraseña debe tener al menos 8 caracteres.")
            if not any(char.isdigit() for char in password):
                raise ValidationError("La contraseña debe contener al menos un número.")
            if not any(char.isupper() for char in password):
                raise ValidationError("La contraseña debe contener al menos una letra mayúscula.")
            if not any(char.islower() for char in password):
                raise ValidationError("La contraseña debe contener al menos una letra minúscula.")
            if not re.search(r'[@#~._!¡?¿]', password.lower()):
                raise ValidationError("La contraseña debe contener al menos un caracter especial.")

        return password

    def clean_timestamp(self):
        timestamp = self.cleaned_data.get("timestamp")

        if timestamp:
            current_time = timezone.now()
            if (current_time - timestamp).seconds > 120:
                raise ValidationError("El formulario no puede enviarse 2 minutos después de haber accedido.")

        return timestamp