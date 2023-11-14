from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

class TuFormulario(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    timestamp = forms.DateTimeField(widget=forms.HiddenInput, required=False)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        timestamp = cleaned_data.get("timestamp")

        # Validación: username y password no pueden coincidir
        if username and password and username == password:
            raise ValidationError("El nombre de usuario y la contraseña no pueden ser iguales.")

        # Validación: password no puede contener el username (case insensitive)
        if username and password and username.lower() in password.lower():
            raise ValidationError("La contraseña no puede contener el nombre de usuario.")

        # Validación: password debe tener una longitud mínima de 8 caracteres
        # y contener un caracter especial, números y letras mayúsculas y minúsculas
        if password:
            if len(password) < 8:
                raise ValidationError("La contraseña debe tener al menos 8 caracteres.")
            if not any(char.isdigit() for char in password):
                raise ValidationError("La contraseña debe contener al menos un número.")
            if not any(char.isupper() for char in password):
                raise ValidationError("La contraseña debe contener al menos una letra mayúscula.")
            if not any(char.islower() for char in password):
                raise ValidationError("La contraseña debe contener al menos una letra minúscula.")
            if not any(char.isalnum() or not char.isalpha() for char in password):
                raise ValidationError("La contraseña debe contener al menos un caracter especial.")

        # Validación: el formulario no debe enviarse 2 minutos después de que se accedió
        if timestamp:
            current_time = timezone.now()
            if (current_time - timestamp).seconds > 120:
                raise ValidationError("El formulario no puede enviarse 2 minutos después de haber accedido.")