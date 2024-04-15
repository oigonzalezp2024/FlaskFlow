
---

# FlaskFlow

***

<b>FlaskFlow</b> es una clase que hereda de la librería <B>Flask</b>. He aplicado herencia a la clase Flask, para que por medio de este proyecto se pueda agregar o simplificar procesos de la misma, y al mismo tiempo tener acceso a todas herramientas presentes y futuras de Flask.

---

## Documentación técnica de FlaskFlow

***

### El método renderJson
> renderJson( name:str='', page:str='', getData:str='./data/data.json' )->None 

| Parametros | ¿Qué es? | 
| :---- | :---- |
| page:str | Nombre de la página a renderizar. |
| name:srt | Titulo de la tabla. |
| getData:str | Path del Json. |

## ¿Qué hace?

Renderiza un Json en una tabla, según la ruta indicada en el parametro <b>page</b>.  
Gracias al diseño inteligente del template:  

>./web-python-flask/templates/index.html  

No será necesario modificar nada en la plantilla para visualizar datos de cualquier tabla, solo enviele el path de un json que se ajuste al diseño formal de una tabla y el lo renderizará.



### Ejemplo de uso
> ./app.py

<pre>
from flaskFlow.flaskFlow import FlaskFlow

app = FlaskFlow(__name__)
@app.route('/')
@app.route('/<name>')
def hello(name=None):
    render = app.renderJson('medicos', 'index.html', './data/data.json')
    return render

</pre>



### Configuración del entorno de desarrollo
| Paso   | Descripción                       | comando                             |
| :----  | :----                             | :---                                |
| Paso 1 |  Crear el entorno de trabajo.     | python -m venv env                  |
| Paso 2 | Activar el entorno de trabajo.    | ./env/Scripts/activate              |
| Paso 3 | Actualizar el gestor de paquetes. | python -m pip install --upgrade pip |
| Paso 4 | Prepare la receta de librerías.   | pip install -r requirements.txt     |
| Paso 5 | Ejecute el programa con debug. | flask run --debug |
| Paso 6 | Dejar de desplegar la web.| Ctrl+C |
***

### Librerías del proyecto
| librería  | Descripción              | Comando                           |
| :----     | :---                     | :---                              |
| Flask | Facilita desarrollo web con python | python -m pip install Flask |

Con la instalación de Flask se instalarán automaticamente las siguientes librerías.
<pre>
blinker==1.7.0
click==8.1.7
colorama==0.4.6
Flask==3.0.3
importlib_metadata==7.1.0
itsdangerous==2.1.2
Jinja2==3.1.3
MarkupSafe==2.1.5
Werkzeug==3.0.2
zipp==3.18.1
</pre>
---

### Realice sus pruebas, actualizaciones o modificaciones
Puedes actualizar, contribuir y mejorar el presente software, es libre. Licencia GNU v3.  
No esta permitido modificar la licencia de trabajos derivados de este proyecto.  
Por norma internacional debes conservar el mismo tipo de licencia.

#### Actualizar la receta.
Si agregas nuevas librerías al proyecto, no olvides actualizar la receta, y de paso, esta documentación, con los detalles de tu gestión.

``` CMD
pip freeze > requirements.txt
```
### Comprobar que todo está en orden
| Paso   | Descripción                                   | comando                               |
| :----  | :----                                         | :---                                  |
| Paso 1 | Desactive el entorno de trabajo.              | deactivate                            |
| Paso 2 | Elimine el entorno anterior.                  | rm -R env                             |
| Paso 3 | Cree un entorno de python.                    | python -m venv env                    |
| Paso 4 | Active el entorno de trabajo.                 | ./env/Scripts/activate                |
| Paso 5 | Actualice el gestor de paquetes.              | python -m pip install --upgrade pip   |
| Paso 6 | Instale las librerías necesarias para operar. | pip install -r requirements.txt       |
| Paso 7 | Realice pruebas de rutina.                    |  flask run --debug |
| Paso 8 | Finalice su gestión.                          | deactivate                            |
| Paso 9 | Dejar de desplegar la web.| Ctrl+C |

