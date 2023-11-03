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