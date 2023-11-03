# Comienzo proyecto
## Entorno virtual

crear un entorno virtual en consola con el comando 
```bash
mkvirtualenv
```
seguido del nombre de el entorno virtual que desees 
## Instalacion
Debes actualizar pip para tener la ultima version (hoy es 3/11/2023)
```bash
python -m pip install --upgrade pip
```
Crear un requirements.txt y añadir "Django~=4.2.7" para despues poner el comando
```bash
pip instal -r requirements.txt
```
Despues poner el comando 
```bash
django-admin startproject mysite .
```
Esto emprezará el proyecto creandote un archivo manage.py y un directorio mysite con varios

## Cambiar la configuarcion por defecto
Ir al archivo "mysite/settings.py" para cambiar la siguiente configuración 
```bash
TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'es-es'
```
Debajo de la línea de codigo
```bash
STATIC_URL = '/static/'
```
Hay que añadir la siguiente línea
```bash
STATIC_ROOT = BASE_DIR / 'static'
```

## Configurar base de datos
Por defecto la base de datos viene configurada asi en el archivo "mysite/settings.py"
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
Hacer las migraciones pertinentes con los siguientes comandos
```bash
python manage.py migrate
```
## Iniciar el servidor

Con el siguiente comando iniciaremos el servidor
```bash
python manage.py runserver
```
## Crear aplicacion

Introducimos el siguiente comnado para iniciar una aplicacion aparte y mantener un orden
```bash
python manage.py startapp task
```
Esto creeara un nuevo directorio con el nombre de task el cual continene la aplicacion

Nos vamos a "mysite/settings.py" y en el apartado de 
```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
Tenemos que añadir al final lo siguiente para que la aplicacion este instalada
```bash
'task',
```
## Creamos un modelo
Vamos a "task/models.py" y escribimos lo siguiente
```python
from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    text = models.TextField()

    created_date = models.DateTimeField(default=timezone.now)

    published_date = models.DateTimeField(blank=True, null=True)

def __str__(self):

    return self.title
```
Creamos los ficheros de migración y lo aplicamos con los siguientes comandos
```bash
python manage.py makemigrations task
python manage.py migrate task
```
Se nos creará un directorio migrations

## Administación
Vamos a "task/admin.py" y añadimos lo siguiente
```python
from .models import Post

admin.site.register(Post)
```
En la consola de comandos creamos un superadministador con el siguiente comando
```bash
python manage.py createsuperuser
```
Nos pedira el nombre del superadministrador, el correo, la contraseña y la confirmación de la contraseña
Si iniciamos el servidor (python manage.py runserver) y en el navegador nos introducimos 127.0.0.1:8000/admin
Nos presentará una pantalla de inicio de sesión, en donde pondremos el usuario y la contraseña anteriormente introducidas
Y nos mostrará una pantalla donde podemos crear tasks

## View Layer
Vamos a "mysite/urls.py" y añadmimos lo siguiente
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
path('admin/', admin.site.urls),
path('', include('blog.urls')),
]
```