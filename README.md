# Blog Django - Pre-entrega 11

Proyecto de un blog web desarrollado con Django. Esta entrega continúa el CRUD
de publicaciones de la pre-entrega 10 y agrega autenticación de usuarios,
registro, perfiles, avatares y protección de las vistas sensibles.

## Repositorio

Este proyecto corresponde a la entrega 11:

- [Repositorio en GitHub](https://github.com/gcostaclases/ch-pre-entrega-11)

El repositorio mantiene una estructura independiente de las entregas anteriores,
como parte de la organización utilizada por el usuario.

## Novedades respecto de la pre-entrega 10

- Se creó la app `accounts` para manejar registros, login, logout y perfiles.
- Se integró el sistema de autenticación de Django.
- Se agregó un formulario personalizado basado en `UserCreationForm`.
- Se creó el modelo `Perfil`, relacionado con `User` mediante
  `OneToOneField`.
- Cada perfil puede guardar una biografía, una página web y un avatar.
- Se configuró la carga de avatares en `media/avatares/`.
- Se agregaron páginas para ver y editar el perfil.
- Se incorporó el cambio de contraseña con las vistas de Django.
- Las vistas para crear, editar y eliminar posts requieren autenticación.
- La edición y eliminación verifican que el usuario sea el autor del post.
- El listado y el detalle de posts siguen siendo públicos.
- El listado y el detalle muestran el avatar del autor o una imagen
  predeterminada.
- El menú cambia según si el usuario inició sesión o no.
- Se agregó un menú de cuenta con avatar y opciones de perfil.
- Se mantuvo el CRUD de posts con imágenes y estados.

## Autenticación y perfiles

### Registro

El usuario puede registrarse desde `/accounts/registro/`. El formulario
personalizado solicita nombre de usuario, email y contraseña. Al guardar el
usuario, la vista crea automáticamente su objeto `Perfil` relacionado.

### Login y logout

Las vistas de autenticación permiten ingresar en `/accounts/login/` y cerrar
sesión desde el menú de la cuenta. Después del login o logout, el proyecto
redirige al listado de posts.

### Perfil

La página `/accounts/perfil/` muestra el usuario, email, biografía y avatar.
Solo puede acceder a ella un usuario autenticado.

Desde `/accounts/perfil/editar/` se pueden modificar la biografía, el enlace
web y el avatar. El formulario procesa archivos mediante
`enctype="multipart/form-data"` y `request.FILES`.

## Organización general del proyecto

La consigna sugería mantener `base.html` dentro de la app `posts`, pero decidí
separar los templates realmente generales del sitio.

La página base, el inicio y Acerca de representan al proyecto completo y son
utilizados por las tres apps. Por eso fueron movidos fuera de `posts`:

```text
templates/
└── project/
    ├── base.html
    ├── inicio.html
    └── acerca.html
```

Los templates propios de cada app se mantienen en su ubicación correspondiente:

```text
posts/templates/posts/
accounts/templates/accounts/
```

Los recursos generales también se separaron de la app `posts`. Los estilos,
el JavaScript de navegación y el logo compartido quedaron en:

```text
static/
└── project/
    ├── css/
    ├── js/
    └── img/
```

Esta organización permite que todos los templates compartan el mismo diseño
sin depender de la carpeta `posts/static`. La imagen `default-post.png`
permanece dentro de `posts/static`, porque corresponde específicamente a los
posts sin imagen.

Para que Django encuentre esa carpeta general, se agregó:

```python
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

Para que Django encuentre la nueva carpeta general, se agregó en `settings.py`:

```python
'DIRS': [BASE_DIR / 'templates'],
```

Esta configuración no reemplaza la búsqueda de templates dentro de las apps:
`APP_DIRS=True` sigue encontrando los templates de `posts` y `accounts`.

Las páginas generales tienen sus vistas propias en
`blog_project/views.py`:

```python
def inicio(request):
    return render(request, "project/inicio.html")


def acerca(request):
    return render(request, "project/acerca.html")
```

Después, las rutas generales se definieron directamente en
`blog_project/urls.py`:

```python
path('', project_views.inicio, name='inicio'),
path('acerca/', project_views.acerca, name='acerca'),
path('posts/', include('posts.urls')),
path('accounts/', include('accounts.urls')),
```

De esta manera, `inicio` y `acerca` ya no dependen de vistas o templates de
la app `posts`. La app `posts` queda encargada únicamente de las publicaciones,
sus modelos, formularios y vistas CRUD.

## Tecnologías utilizadas

- Python
- Django 6.1.3
- Pillow 13.0.0
- HTML5
- CSS3
- JavaScript mínimo para el menú de cuenta
- SQLite

## Estructura principal

```text
blog_django/
├── manage.py
├── README.md
├── requirements.txt
├── db.sqlite3
├── media/
│   ├── posts/
│   └── avatares/
│
├── blog_project/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── asgi.py
│   └── wsgi.py
│
├── templates/
│   └── project/
│       ├── base.html
│       ├── inicio.html
│       └── acerca.html
│
├── static/
│   └── project/
│       ├── css/
│       │   └── style.css
│       ├── js/
│       │   └── main.js
│       └── img/
│           └── logo-glups.png
│
├── posts/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   ├── templates/
│   │   └── posts/
│   └── static/
│       └── posts/
│           └── img/
│               └── default-post.png
│
└── accounts/
    ├── admin.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    ├── views.py
    ├── migrations/
    └── templates/
        └── accounts/
```

## Rutas disponibles

| Ruta | Página | Acceso |
| --- | --- | --- |
| `/` | Página de inicio | Público |
| `/acerca/` | Información sobre el proyecto | Público |
| `/posts/` | Listado de posts publicados | Público |
| `/posts/<slug>/` | Detalle de un post | Público |
| `/posts/crear/` | Crear un post | Requiere login |
| `/posts/<slug>/editar/` | Editar un post | Requiere login y ser autor |
| `/posts/<slug>/eliminar/` | Eliminar un post | Requiere login y ser autor |
| `/accounts/registro/` | Crear una cuenta | Público |
| `/accounts/login/` | Iniciar sesión | Público |
| `/accounts/logout/` | Cerrar sesión | Usuario autenticado |
| `/accounts/perfil/` | Ver perfil | Requiere login |
| `/accounts/perfil/editar/` | Editar perfil | Requiere login |
| `/accounts/password/cambiar/` | Cambiar contraseña | Requiere login |
| `/admin/` | Panel de administración | Staff |

## Configuración de archivos multimedia

Los posts utilizan `ImageField` con archivos guardados en `media/posts/`.
Los avatares utilizan `ImageField` con archivos guardados en
`media/avatares/`.

En `settings.py` se configuró:

```python
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

Las rutas media se sirven durante el desarrollo cuando `DEBUG=True`.

## Protección de rutas

La creación, edición y eliminación de posts están protegidas con
`@login_required`. Además, las vistas de edición y eliminación verifican que
`post.autor == request.user` para impedir modificaciones de publicaciones
ajenas.

Las páginas de perfil y edición de perfil también utilizan `@login_required`.
Si un usuario anónimo intenta ingresar, Django redirige a la página de login.

## Instalación y ejecución

### 1. Crear el entorno virtual

Windows:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

macOS o Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 3. Aplicar las migraciones

```bash
python manage.py migrate
```

### 4. Crear un superusuario

```bash
python manage.py createsuperuser
```

### 5. Ejecutar el servidor

```bash
python manage.py runserver
```

Abrir [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Cómo probar el flujo completo

1. Registrarse desde `/accounts/registro/`.
2. Iniciar sesión desde `/accounts/login/`.
3. Entrar al perfil y completar la biografía.
4. Subir un avatar desde editar perfil.
5. Crear una publicación desde `/posts/crear/`.
6. Verificar que el avatar y el nombre del autor aparecen en el listado y detalle.
7. Editar o eliminar únicamente los posts propios.
8. Cerrar sesión desde el menú de cuenta.
9. Comprobar que las rutas protegidas redirigen al login.
10. Entrar al panel de administración y revisar usuarios y perfiles.

El listado y el detalle continúan visibles para visitantes sin autenticación.
