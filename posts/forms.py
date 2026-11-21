from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    # Le hago un constructor para personalizar los textos del widget de imagen
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        image_widget = self.fields["imagen"].widget
        image_widget.initial_text = "URL"
        image_widget.input_text = "Cambiar imagen"
        image_widget.clear_checkbox_label = "Eliminar imagen"

    # La clase Meta le indica a Django qué modelo debe usar y qué campos deben aparecer en el formulario
    class Meta:
        model = Post
        fields = ["titulo", "contenido", "estado", "imagen"]

    labels = {
        "titulo": "Título del post",
        "contenido": "Contenido",
        "autor": "Autor del post",
        "estado": "Estado de publicación",
        "imagen": "Imagen destacada",
    }

    widgets = {
        "titulo": forms.TextInput(attrs={
            "placeholder": "Escribe el título del post"
        }),
        "contenido": forms.Textarea(attrs={
            "placeholder": "Escribe el contenido del post",
            "rows": 6
        }),
        "autor": forms.TextInput(attrs={
            "placeholder": "Nombre del autor"
        }),
    }

    def clean_titulo(self):
        titulo = self.cleaned_data["titulo"]

        if len(titulo) < 5:
            raise forms.ValidationError(
                "El título debe tener al menos 5 caracteres.")

        return titulo
