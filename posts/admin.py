from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.site_header = "Administración de Mi Blog"
admin.site.site_title = "Panel del Blog"
admin.site.index_title = "Gestión de contenidos"

@admin.register(Post)
# Esta clase permite mostrar columnas útiles en la lista del admin
class PostAdmin(admin.ModelAdmin):
    # Define qué columnas se mostrarán en la lista de administración
    list_display = ("titulo", "autor", "fecha_creacion", "estado")
    # Agrega un campo de búsqueda para buscar por título, contenido o autor
    search_fields = ("titulo", "contenido", "autor")
    # Agrega filtros para ordenar por estado o fecha de creación
    list_filter = ("estado", "fecha_creacion")
    # Permite editar el estado directamente desde la lista (sin necesidad de entrar al detalle del post)
    # Importante: el campo incluido en list_editable también debe estar en list_display.
    list_editable = ("estado",)
    # Permite generar automáticamente el slug a partir del título al crear un nuevo post en el admin.
    # Acá se ve solo el titulo pero en realidad se guarda el titulo + el id del post para asegurar que sea único.
    prepopulated_fields = {"slug": ("titulo",)}

    # NOTA: Siempre revisar que los nombres usados en list_display, search_fields y list_filter existan realmente en el modelo.
