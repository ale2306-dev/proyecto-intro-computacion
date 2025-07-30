# PROYECTO FINAL - INTRODUCCIÓN A LA COMPUTACIÓN

#### Hernan Parra - 31.466.113 - Física

--------------------------
### Explicación:

Este proyecto consta de dos aplicaciones, una aplicación que trabaja en la consola y otra que tiene implementada una interfaz gráfica con StreamLit.

--------------------------
### Proyecto solo en consola:

En la carpeta **Proyecto solo consola** se encuentra un archivo **proyecto.py** que contiene todo el código del proyecto. Este está organizado en funciones que cumplen estrictamente con los lineamientos del proyecto. 

De esta forma, cada una de las funciones equivale a una opción del menú.

-----------------------------

### Proyecto con interfaz gráfica

En la carpeta **Proyecto con StreamLit** se encuentra el proyecto adaptado a una interfaz gráfica. 

El proyecto está organizado de la siguiente manera:

- **requirements.txt**: archivo con las librerias necesarias para el correcto funcionamiento de la aplicación. Se recomienda instalar las librerias desde un entorno virtual.

- **app.py**: aplicación principal. En este archivo se organiza la estructura de la aplicación
- **components**: aquí se encuentran las funciones esenciales de la aplicación, en archivos separados.
- **views**: aquí se encuentran las vistas del programa. Cada archivo corresponde a una ventana (son dos, ***Manejo del CSV*** y ***Gráficos***), estos archivos gestionan la estructura de cada una de ellas.

##### Modo de uso:

***(Opcional)***:  En caso de no tener las librerias necesarias instaladas, cree un entorno virtual escribiendo el siguiente comando en el terminal:

###### *(Asegurese de estar posicionado en la carpeta donde se encuentra app.py)*
> `python -m venv .venv`

Una vez creado el entorno, active el mismo ejecutando el script de activación, comunmente suele ser:

> `.venv/Scripts/activate` o `.venv/bin/activate`

Una vez activado, procede a instalar las librerias necesarias:

> `pip install -r requirements.txt`

En caso de tener las librerias instaladas se recomienda igualmente realizar estos pasos, a manera de evitar problemas con las librerias.

***Iniciar Aplicación***: 

Asegurese de estar posicionado en la misma carpeta donde se encuentra el archivo **app.py**

Escriba en la terminal el siguiente comando para iniciar la aplicación:

> `streamlit run app.py`

donde ***app.py*** es el archivo principal del proyecto

------------------------

**Listo! ya tienes el explorador de datos climáticos corriendo**

El programa se abrirá directamente en su navegador predeterminado, en caso de que no, copie la dirección que arroja el terminal y peguela en su navegador de confianza.
