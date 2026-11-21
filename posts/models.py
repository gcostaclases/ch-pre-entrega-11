from django.db import models
from django.conf import settings
from django.utils.text import slugify

# Create your models here.
class Post(models.Model):
    ESTADOS = [
        ("borrador", "Borrador"),
        ("publicado", "Publicado"),
        ("archivado", "Archivado"),
    ]

    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=20, choices=ESTADOS, default="borrador")
    slug = models.SlugField(max_length=220, unique=True, blank=True, null=True)
    imagen = models.ImageField(upload_to="posts/", null=True, blank=True)

    # La clase Meta permite configurar comportamientos del modelo, como el orden por defecto.
    # Esto ordena los posts por fecha de creación en orden descendente
    class Meta:
        ordering = ["-fecha_creacion"]

    # Slug con la suma del id del post al final para asegurar que sea único, incluso si hay títulos repetidos.
    def save(self, *args, **kwargs):
        if self.pk is None:
            # Ignora el slug preliminar generado por el admin
            self.slug = None
            super().save(*args, **kwargs)  # Obtiene el ID

            self.slug = f"{slugify(self.titulo)}-{self.pk}"
            super().save(update_fields=["slug"])
        else:
            super().save(*args, **kwargs)

    # Esto es como el toString()
    def __str__(self):
        return self.titulo
