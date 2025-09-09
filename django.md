# Django

Django es un framework que se ejecuta sobre Python.

## Pasos para instalar Django

1. Instala Django:
    ```bash
    sudo apt install python3-django
    django-admin --version
    ```

## Crear y activar un entorno virtual

1. Crea el entorno virtual:
    ```bash
    python3 -m venv nombre_entorno
    ```
2. Actívalo:
    ```bash
    source nombre_entorno/bin/activate
    ```

## Dentro del entorno virtual

- Instala Django:
    ```bash
    pip install django
    ```
- Crea un proyecto en el directorio actual:
    ```bash
    django-admin startproject mysite .
    ```
- Crea una aplicación:
    ```bash
    python3 manage.py startapp nombre_app
    ```
- Levanta el servidor:
    ```bash
    python3 manage.py runserver numero_puerto
    ```
- Ayuda de comandos:
    ```bash
    python3 manage.py --help
    ```
- Migraciones:
    ```bash
    python3 manage.py makemigrations   # Después de editar models.py
    python3 manage.py migrate          # Ejecuta todas las migraciones
    ```

## Conceptos clave

- Al crear una carpeta en Django, se crea un proyecto.
- Los proyectos en Django se dividen en distintas aplicaciones.

## Manipulación de datos desde la shell de Django

1. Accede a la shell:
    ```bash
    python3 manage.py shell
    ```
2. Ejemplos de uso:
    ```python
    from nombre_proyecto import ClaseModelo
    variable = ClaseModelo(name="Aplicacion Movil")  # Inserción de datos
    variable.save()                                  # Guardado de datos
    ClaseModelo.objects.all()                        # Listado de datos
    ClaseModelo.objects.get(id=1)                    # Buscar por campo específico
    p.task_set.create(title="desarrollar login")     # Asignar tarea a un proyecto
    p.task_set.all()                                 # Todas las tareas del proyecto
    p.task_set.get(id=1)                             # Filtrar tarea por id
    ClaseModelo.objects.filter(name__startswith="aplicacion")  # Filtrar por nombre
    ```

## Panel administrativo

- Crea un superusuario para acceder al panel administrativo:
    ```bash
    python3 manage.py createsuperuser
    ```

## Plantillas

- Django utiliza el motor de plantillas llamado Jinja2.

## Django REST Framework

- Django REST Framework se ejecuta sobre Django.
- Crea un archivo `serializers.py` para definir serializadores.
- El `ViewSet` determina quién puede consultar el serializador.

## S4 - URLs y Vistas

- Para acceder a una vista, debes definir una URL en un archivo `urls.py` dentro de la app:

    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('quotes/', views.index, name='index')
    ]
    ```

- Incluye este archivo de URLs en la app principal:

    ```python
    path('', include('quotes.urls')),
    ```

#### Funcion regresiva

- La funcion reverse de Django se utiliza para obtener la URL de una vista a partir de su nombre (el nombre que le diste en tu archivo urls.py). Es muy útil para evitar escribir rutas manualmente y mantener tu código más flexible y mantenible.

**¿Qué es?**

- Reverse busca el nombre de la vista en tus URLs y construye la URL correspondiente. Así, si cambias la URL en urls.py, no tienes que actualizarla en todo tu código, solo usas el nombre.

```py
reverse("name-url", args = [params])
```

## S5 - Templates

#### Registrando un template.

- Se pueden hacer de dos formas:
  1. Registrando la app (`landing`) en `config/settings.py` dentro del arreglo `INSTALLED_APPS`.

  ```py
  # Primera forma de registrar la aplicacion.
  INSTALLED_APPS = [
    'landing',
  ]
  ```
  2. Registrando directamente cada plantilla en el arreglo de `TEMPLATES`.

  ```py
    # Primera forma de registrar la aplicacion.
    TEMPLATES = [
        {
            'DIRS': [
                # Se puede hacer de esta manera pero el detalles es que hay que importar una a una los templates que deseas ocupar
                BASE_DIR / "landing" / "templates"
            ],
        },
    ]
  ```

#### Renderizando templates

- Para renderizar templates en Django, se usa la función render dentro de una vista. Esta función combina un archivo HTML (template) con un contexto (datos) y devuelve una respuesta HTTP.

Ejemplo:

```py
# views.py
from django.shortcuts import render

def mi_vista(request):
    contexto = {'nombre': 'Juan'}
    return render(request, 'mi_template.html', contexto)
```

/explain
Explicame en breve como se renderizan los templates en Djgano?

Para renderizar templates en Django, se usa la función render dentro de una vista. Esta función combina un archivo HTML (template) con un contexto (datos) y devuelve una respuesta HTTP.

Ejemplo básico:

- **'mi_template.html'** es el archivo de template.
- contexto es un diccionario con los datos que se pasan al template.
- Django busca el template en las carpetas configuradas en TEMPLATES en settings.py.

#### Django Template Language e interpolación de variables

Django Template Language (DTL) es el sistema de plantillas que utiliza Django para generar HTML dinámico. Permite:

- Separar la lógica de presentación (cómo se muestra la información) de la lógica de negocio (cómo se procesa la información).
- Crear páginas web dinámicas fácilmente.

**Interpolación de variables en DTL:**

- Consiste en insertar valores de variables de Python (por ejemplo, datos de una base de datos) directamente en el HTML.
- Se realiza usando doble llave: `{{ variable }}`

**Ejemplo:**

```html
<p>Hola, {{ nombre }}!</p>
```

Esto mostrará el valor de la variable `nombre` en el HTML generado.

#### Filtros

- Los filtros son decoradores que se aplican a las variables que se le pasan por medio de la view al template.

**Ejemplo:**

```html
<p>Hola, {{ nombre | upper }}!</p>
```