from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_posts, name="lista_posts"),
    path("crear/", views.crear_post, name="crear_post"),
    path("<slug:slug>/editar/", views.editar_post, name="editar_post"),
    path("<slug:slug>/eliminar/",
         views.eliminar_post, name="eliminar_post"),
    path("<slug:slug>/", views.detalle_post, name="detalle_post"),
]
