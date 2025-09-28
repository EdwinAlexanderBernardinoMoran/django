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

#### Tags

Los tags en Django Template Language (DTL) son instrucciones especiales que controlan la lógica dentro de los templates, como bucles, condicionales o la inclusión de otros archivos. Se escriben entre `{% %}`.

- En los templates puedes acceder a los valores atravez del punto como si fuera un objeto auque sean listas

```html
<ul>
    <li>{{ stacks.0 }}</li>
</ul>
```

**Ejemplos comunes de tags:**

- **for**: Para iterar sobre una lista.
    ```html
    {% for item in lista %}
      <p>{{ item }}</p>
    {% endfor %}
    ```

- **if**: Para condicionales.
    ```html
    {% if usuario_activo %}
      <p>Bienvenido, usuario activo.</p>
    {% else %}
      <p>Por favor, activa tu cuenta.</p>
    {% endif %}
    ```

- **include**: Para incluir otro template.
    ```html
    {% include "header.html" %}
    ```

- **block** y **extends**: Para herencia de templates.
    ```html
    {% extends "base.html" %}
    {% block contenido %}
      <p>Contenido específico de la página.</p>
    {% endblock %}
    ```

- **url tag**: Nos ayudan a no escribir toda una url completa.
    - Define una url

    ```py
        path('stack/<str:tool>', views.stack, name='stack')
    ```

    - Define el metodo en el view

    ```py
        def stack(request, tool):
            return HttpResponse(f"Estás utilizando la herramienta: {tool}")
    ```

    - Uso en el template

    ```html
    <ul>
        {% for item in stacks %}
            <li><a href="{% url 'stack' item.name %}">{{ item.name }}</a></li>
        {% empty %}
            <li>No hay tecnologías disponibles</li>
        {% endfor %}
    </ul>
    ```

#### Herencia de templates (Block tag)

- Es una plantilla base de la cual dependen todos los demas, es necesario crear una carpeta `templates` en la raiz, seguido del nombre de la app(landing), para que Django lo puedo identificar, en este caso es similar a Laravel pero para que Django lo reconosca es necesario registrarlo en los `settings.py`.

```py
TEMPLATES = [
    {
        'DIRS': [
            # Se puede hacer de esta manera pero el detalles es que hay que importar una a una los templates que deseas ocupar
            # BASE_DIR / "landing" / "templates"

            BASE_DIR / "templates"
        ],
    },
]
```

#### Ejercicio
- Crea una carpeta en la raiz del proyecto llamada `templates/name.html` ahi crea la estructura base.
- Registra este template principal en el archivo `settings.py` en `TEMPLATES.DIRS` para que Django lo reconosca.
- Primero crea una carpeta dentro de tu app llamada `templates/name_app`, dentro crea un archivo de preferencia `name_app.html`
- Registra el template en el archivo `settings.py` en `INSTALLED_APPS`
- Crea un url para tu pagina principal en caso no la tengas.

#### Fragmentos de templates (include tag)

- Nos permite poder incorporar trozos de codigos reutilizables dentro de cualquier archivo html.
- Crea una carpeta llamada `quotes/templates/quotes/includes/partial.html`

**Ejemplo de importacion**
```html
{% include './includes/partial.html' with name=name day_weeks=day_weeks %}
```

#### Template 404

- Crea un archivo 404.html en la siguiente ruta `templates/404.html`
- Automaticamente Django reconocera que existe ese archivo para poder mostrarlo en pantalla.

```py
def days_weeks(request, day):
try:
    return HttpResponse(days_of_week[day])
except KeyError:
    raise Http404()
```

**Importante!**: Asegúrate de que DEBUG = False en tu archivo settings.py para que Django use tu template 404 personalizado en producción.

#### Archivos estaticos

- Es necesario que el paquete `django.contrib.staticfiles` este instalado y configurado correctamente en el archivo `settings.py` en `INSTALLED_APPS = []`.
- La variable `STATIC_URL` no funciona en modo de desarrollo solo funciona en produccion.
- Dentro de cada app crea una carpeta llamada `quotes/static/quotes/styles.css`.
- Luego en la plantilla base es necesario agregar un `block` para poder agregar ahi los archivos personalizados.

```html
<!-- Archivo base o layout principal -->
{% block page_styles %}{% endblock page_styles %}
```

```html
<!-- Carga de archivos estaticos dentro del html personalizado-->
{% load static %}

{% block page_styles %}
    <link rel="stylesheet" href="{% static 'quotes/styles.css' %}">
{% endblock page_styles %}
```

#### Archivos estaticos globales

- Crea una carpeta a nivel global llamada `static` si quieres crea una carpeta por cada tipo de documento.
- Luego carga los archivos estaticos en el layout principal.

```html

<!-- Antes del DOCTYPE -->
{% load static %}

<link rel="stylesheet" href="{% static 'css/styles.css' %}">
```

- Es necesario que Django sepa donde estan los archivos que quiero cargar de la siguiente manera.

```py
# Añadimos la ruta de los archivos estáticos globales
STATICFILES_DIRS = [
    BASE_DIR / "static",

    # Podemos agregar cuantas urls sean necesarias.
]
```

## S3 - Modelos y Base de Datos

#### Que es un ORM y como funciona en Django?
- Object-Relational Mapping (ORM), es una herramienta que permite trabajar con base de datos utilizando clases y objetos en un lenguaje deprogramacion, en lugar de usar SQL directamente.

    Clases = Tablas
    Atributos = Columnas
    Instancias = Filas

- Cada clase que hereda de `models.Model` se convierte en una tabla en la base de datos.

```py
class Book(models.Model):
    title = models.CharField(max_length=200)
```

- Equivalencia entre SQL y Django ORM

```sql
INSERT INTO books (title, publication_year) VALUES ('1984', 1949)
```

```py
# Create
Book.objects.create(title="1984", publication_year=1949)

# Select
Book.objects.all()

# Filter
Book.objects.filter(author__name="Orwell")
```

#### Tipos de campos y parametros

En Django, los tipos de campos y parámetros se utilizan para definir la estructura de los modelos que representan tablas en la base de datos. 

[Tipos de Campos](https://docs.djangoproject.com/en/5.2/ref/models/fields/#field-options)

**Tipos de campos comunes en Django:**
- `CharField`: Almacena cadenas de texto de longitud limitada.
- `TextField`: Almacena texto de longitud ilimitada.
- `IntegerField`: Almacena números enteros.
- `FloatField`: Almacena números de punto flotante.
- `BooleanField`: Almacena valores booleanos (`True` o `False`).
- `DateField`: Almacena fechas.
- `DateTimeField`: Almacena fechas y horas.
- `EmailField`: Almacena direcciones de correo electrónico.
- `ForeignKey`: Define una relación muchos-a-uno con otro modelo.
- `ManyToManyField`: Define una relación muchos-a-muchos con otro modelo.
- `OneToOneField`: Define una relación uno-a-uno con otro modelo.

[Tipos de Parametros](https://docs.djangoproject.com/en/5.2/ref/models/fields/#field-options)

**Parámetros comunes de los campos:**
- `max_length`: Longitud máxima del campo (usado en `CharField`).
- `null`: Permite valores nulos en la base de datos.
- `blank`: Permite que el campo esté vacío en formularios.
- `default`: Valor por defecto del campo.
- `choices`: Opciones predefinidas para el campo.
- `unique`: Garantiza que el valor sea único en la tabla.
- `primary_key`: Define el campo como clave primaria.

Estos campos y parámetros permiten personalizar cómo se almacenan y validan los datos en la base de datos a través de los modelos de Django.

[Mas Informacion](https://www.geeksforgeeks.org/python/django-model-data-types-and-fields-list/)

#### Creando modelos y migraciones

- Los modelos se crean en el archivo `models.py`.

```py
class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
```

- Luego de crear los modelos ejecuta el comando `python3 manage.py makemigrations name-app`.
- Ejecuta las migraciones con el comando `python3 manage.py migrations`.
- Ejecuta `python3 manage.py showmigrations`.

#### Shell en Django

- La shell de Django es una consola interactiva de Python que carga automáticamente el entorno de tu proyecto Django. Permite ejecutar código Python y acceder a tus modelos, consultar la base de datos, probar funciones y depurar tu aplicación de manera rápida.

- Para abrir la shell de Django, usa este comando en la terminal desde la raíz de tu proyecto:

```shell
python manage.py shell
```

## S8 - Manipulacion de datos con el ORM

#### Creacion de registros con el ORM usando create

- Esto crea de forma directa el registro.
```py
Author.objects.create(name="Edwin Alexander", birth_date="2002-06-25")
```

#### Creacion de registros con el ORM usando save

- Esto solo crea una instancia del objeto, puedes manipular los datos luego antes de guardarlo.

```py
rowling = Author(name="J. K. Rowling", birth_date="1965-07-31")
rowling.name.upper()
rowling.save() # Guardando los datos en la bd.
```

#### Crear registros en lote

- Crear registros en lote en Django significa insertar múltiples registros en la base de datos en una sola operación, en lugar de guardar cada objeto individualmente. Esto se logra usando el método `bulk_create()` del ORM, lo que mejora el rendimiento al reducir la cantidad de consultas a la base de datos.

**Ejemplo:**

```py
Book.objects.bulk_create([
... Book(title="Django RestFramework", publication_date="2025-01-01", author=rowling, pages=250, isbn="1234987"),
... Book(title="Curso de python", publication_date="2025-05-12", author=rowling, pages=100, isbn="1254679")
])
```

```py
# Usando save:
start = time.time() 
for i in range(1000): 
	book = Book( title=f"Libro lento {i}", publication_date="2000-01-01", author=author, pages=100, isbn=f"123456{i}" ) 
	book.save() 
end = time.time() 
print(f"Tiempo usando .save(): {end - start:.2f} segundos")


# Usando bulk_create():
start = time.time() 
books = [] 
for i in range(1000): 
    books.append(Book( title=f"Libro rápido {i}", publication_date="2000-01-01", author=author, pages=250, isbn=f"98765{i}" )) 

Book.objects.bulk_create(books) 
end = time.time() 
print(f"Tiempo usando bulk_create(): {end - start:.2f} segundos")
```

#### Creando registros de forma segura

- Este metodo nos ayuda a evitar duplicacion de datos y actualizar los datos de manera segura en caso no exista podemos crearlo sin ningun problema.

```py

# Obtiene el dato si no existe lo crea
edwin = Author.objects.get_or_create(name="Edwin Alexander", defaults={"birth_date":"1995-08-10"})

# Actualiza el dato si no existe lo crea
elizabeth = Author.objects.update_or_create(name="Elizabeth Perez", defaults={"birth_date":"2002-08-10"})
```

#### Consultas basicas con el ORM

- **Obtener todos los registros**:
    ```py
    Author.objects.all()
    ```

- **Obtener un solo registro (por campo único)**
    ```py
    Author.objects.get(id=1)
    ```

- **Obtener el primer y último registro**
    ```py
    Author.objects.first()
    Author.objects.last()
    ```

- **Ordenar resultados**
    ```py
    Author.objects.order_by('name')  # Ascendente
    Author.objects.order_by('-name') # Descendente
    ```

- **Filtrar registros por campo**
    ```py
    author = Author.objects.filter(name="Edwin Alexander") # Case Sensitive
    author = Author.objects.filter(name__iexact="Edwin Alexander") # Case Insensitive

    # Busqueda por coincidencia parcial.
    author = Author.objects.filter(name__contains="Alexander") # Permite buscar si alguna palabra coincide en el campo.
    author = Author.objects.filter(name__endswith="Alexander") # Busca informacion cuyo nombre en este caso empieza con Alexander
    author = Author.objects.filter(name__startswith="Ale") # Busca informacion cuyo nombre en este caso termina con Alexander
    author = Author.objects.filter(name__startswith="Alexander").exists() # Verifica si existe un registro con cuya busqueda y regresa TRUE o FALSE
    author.query # Imprime la consulta SQL
    ```

- **Filtrar por rango**
    ```py
    author = Author.objects.filter(id__in=[1, 2, 3, 4]) # Trae todos los autores que encuetre
    author = Author.objects.filter(id__gt=10) # Trae todos los autores que cuyo id es mayor a 10
    author = Author.objects.filter(id__gte=10) # Trae todos los autores que cuyo id es mayor o gual a 10
    author = Author.objects.filter(id__lt=10) # Trae todos los autores que cuyo id es menor a 10
    author = Author.objects.filter(id__lte=10) # Trae todos los autores que cuyo id es menor o igual a 10
    ```
- **Filtrando por fechas**

    ```py
    from datetime import date

    Book.objects.filter(publication_date=date(2025,1,1))

    # En caso el campo no sea de tipo fecha puedes a gregar la siguiente palabra asi despues del nombre del campo (publication_date__date) si es de tipo fecha entonces va a tronar
    Book.objects.filter(publication_date__date=date(2025,1,1))

    # Por año
    Book.objects.filter(publication_date__year=2025)

    # Por día
    Book.objects.filter(publication_date__day=11)

    # Mayores al 2010
    Book.objects.filter(publication_date__gt=date(2010,1,1))

    # Menores a 1990
    Book.objects.filter(publication_date__lt=date(1990,1,1))
    ```
- **Consultas Q**

    Las consultas Q en Django permiten construir consultas más complejas usando operadores lógicos como AND, OR y NOT. Son útiles cuando necesitas combinar múltiples condiciones en un solo filtro, especialmente cuando las condiciones son alternativas o excluyentes.

    ```py
    from django.db.models import Q

    Book.objects.filter(Q(title__icontains="software") | Q(title__icontains="prisionero"))

    # Relacion con el author
    Book.objects.filter(Q(title__icontains="prisioner") | Q(author__name__icontains="Edwin"))
    ```

- **Consultas F**

Las consultas F en Django utilizan objetos `F` para referenciar valores de otros campos del mismo modelo directamente en la base de datos, permitiendo realizar operaciones y comparaciones entre campos sin traer los datos a Python. Son útiles para actualizar valores en función de otros campos y para realizar consultas más eficientes.


```py
from django.db.models import F

# Actualizar el campo 'pages' sumando 10 a su valor actual
Book.objects.update(pages=F('pages') + 10)

# Filtrar libros donde 'pages' es mayor que 'publication_year'
Book.objects.filter(pages__gt=F('publication_year'))
```

Esto permite que las operaciones se ejecuten directamente en la base de datos, optimizando el rendimiento y evitando condiciones de carrera.

- **Actualizacion de registros**

```py

# Forma de actualizar registros
author = Author.objects.get(name="Alexander")
author.name = "Edwin"
author.save()

# ¡ Actualiza todos los libros que sean de "Edwin" !
Book.objects.filter(author__name="Edwin").update(title="Titulo actualizado")

```

- **Eliminar registros**

```py

# Elimina el recurso de forma individual.
book = Book.objects.get(title="El poder de la imagen publica")
book.delete()

# Filtra por año y que sean menores al año proporcionado.
Book.objects.filter(publication_date_year__lt=2001).delete()
```


- El argumento on_delete se usa en campos ForeignKey para definir qué sucede cuando el objeto relacionado es eliminado. Aquí tienes los tipos principales de comportamientos de on_delete:

- **CASCADE**: Elimina también los objetos que dependen del objeto borrado.  
- **PROTECT**: Impide borrar el objeto relacionado si existen dependientes; lanza una excepción.  
- **SET_NULL**: Establece el campo como `NULL` si el objeto relacionado se elimina (requiere `null=True`).  
- **SET_DEFAULT**: Asigna el valor por defecto al campo si el objeto relacionado se elimina (requiere `default`).  
- **SET()**: Permite asignar una función o valor personalizado al campo cuando el objeto relacionado se elimina.  
- **DO_NOTHING**: No realiza ninguna acción; puede causar errores de integridad referencial.

- **Soft Delete**

Sirve cuando se quiere conservar los datos pero ocultarlos del sistema. No se borra como tal

```py
# Ejemplo del soft delete
class Book(models.Model):
    title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

```

- **Eliminar registros con relaciones**

```py
# Se elimina tambien los libros del author en caso en la relacion esten en CASCADE
author = Author.objects.get(name="Antonio Cuellar")
author.delete()
```

- **Aggregate**

- Es una forma para aplicar funciones agregadas al SQL se utilizan para calcular valores resumidos directamente en la base de datos, como sumas, promedios, conteos, mínimos y máximos. Esto es útil cuando necesitas obtener estadísticas o resultados globales sin traer todos los registros a Python.

- Ejecuta el cálculo en la base de datos, lo que es más eficiente.
- Evita cargar todos los registros en memoria.

```py
from django.db.models import Count, Sum, Avg, Min, Max

# Contar libros
Book.objects.aggregate(total=Count('id'))

# Sumar páginas
Book.objects.aggregate(total_pages=Sum('pages'))

# Promedio de páginas
Book.objects.aggregate(avg_pages=Avg('pages'))

# Mínimo y máximo de páginas
Book.objects.aggregate(min_pages=Min('pages'), max_pages=Max('pages'))
```

- **Annotations**

- Nos da metrica por objeto(por registros) agrega una columna virtual a cada una de las instancias de la consulta.

- Para mostrar datos agregados junto a cada registro (por ejemplo, cantidad de libros por autor).
- Para realizar cálculos dinámicos sin modificar el modelo.
- Para optimizar consultas evitando cálculos en Python.

```py
from django.db.models import Count

# Agrega un campo 'num_books' a cada autor con la cantidad de libros relacionados
authors = Author.objects.annotate(num_books=Count('books')) # Books viene de la relacion de Book y author

for author in authors:
    print(author.name, author.num_books)
```

**¡Importante!**

Los agregations nos dan informacion global, si queremos informacion registro por registro utilizemos annotations.


- **Transactions Atomic**

Es un conjunto de operaciones en base de datos que se ejecutan todas juntas, en caso de que alguna falle se ejecuta un roolback se deshace todo lo hecho.

```py
from django.db import transaction

# En caso llegue a fallar no se ejecuta ninguna operacion
with transaction.atomic()
    author = Author.objects.create(
        name="Edwin",
        birth_date="2002-10-28"
    )
    Book.objects.create(
        title="Django",
        publication_date="2025-10-10",
        author=author,
        pages=250,
        isbn="25466884"
    )

```

## S9 - Relaciones entre modelos

#### Relaciones uno a muchos (Foreign Key)

Se refiere a una estructura donde un registro de un modelo puede estar relacionado con múltiples registros de otro modelo. Esto se implementa usando el campo ForeignKey.

- **ForeignKey**: Crea una columna author_id en la tabla de books, relaciona cada libro con un author.

```py
class Autor(models.Model):
    nombre = models.CharField(max_length=100)

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='books')
```

#### Relaciones muchos a muchos (ManyToManyField)

Se usan cuando una instancia de un modelo puede estar relacionada con varias instancias de otro modelo, y viceversa. Por ejemplo, un genero puede estar en varios libros, y un libro puede tener varios generos. En Django, esto se implementa usando el campo `ManyToManyField`. Este campo crea automáticamente una tabla intermedia en la base de datos para gestionar las relaciones.

```py
class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    genres = models.ManyToManyField(Genre, related_name='books')

    def __str__(self):
        return self.title
```

- Forma de asignar datos a la relacion.

```bash

ficcion = Genre.objects.get(id=1)
drama = Genre.objects.get(id=2)

bookOne = Book.objects.get(id=1) # Puedes crear uno

# Asignando genero al libro
bookOne.add(ficcion,drama)

# Obteniendo todos los generos relacionados al libro
bookOne.genres.all()

# Obteniendo todos los libros de un genero
ficcion.books.all()
```

#### Relacion uno a uno(One to One)

Es un tipo de relación entre dos modelos donde cada instancia de un modelo está asociada con una sola instancia de otro modelo, y viceversa. Se utiliza el campo `OneToOneField` en uno de los modelos.

```bash
bookOne = Book.objects.get(id=1) # Puedes crear uno

detail = BookDetail.objects.create(summary="New summary", cover_url="http://www.google.com/image.jpg", language="Español", book=book)
```

#### Select related

Unicamente funciona para `Foreign Key` y `OneToOneField` esto hace un join a la misma consulta y carga los objetos relacionados en una sola llamada en lugar de cargarlos uno por uno.

```py
books = Book.objects.select_related("author")
```

#### Prefecth related

`prefetch_related` es un método del ORM de Django que se utiliza para optimizar consultas cuando trabajas con relaciones de tipo `ManyToManyField` o relaciones inversas de `ForeignKey`. Permite obtener los objetos relacionados en una sola consulta adicional, evitando así el problema de N+1 consultas.

**¿Cuándo usarlo?**
- Cuando necesitas acceder a objetos relacionados de tipo muchos a muchos o relaciones inversas y quieres evitar múltiples consultas a la base de datos.

```py
# Supongamos que Book tiene una relación ManyToMany con Genre
books = Book.objects.prefetch_related('genres')

for book in books:
    # No hará una consulta por cada book, ya que los géneros ya están precargados
    print(book.title, [genre.name for genre in book.genres.all()])
```

```py
genres = Genre.objects.prefecth_related("books")

for genre in genres:
    books = genre.books.all()
```

**Diferencia con `select_related`:**
- `select_related` se usa para relaciones `ForeignKey` y `OneToOneField` (hace un JOIN).
- `prefetch_related` se usa para relaciones `ManyToManyField` y relaciones inversas (hace consultas separadas y las une en Python).