# librerías python para entorno grafico
Las librerias hacen el trabajo más facil, son herramientas ya elaboraas que podemos utilizar entres pasos
instalar, importar y utilizar

## guizero
Desde la libreria se importan las funciones para la ventana, el texto y los botones
```py
from guizero import App, Text, PushButton
```
Se crea un objeto tipo App para poner allí todo el contenido de la ventana
```py
app = App(title="Hello world")
```
Se puede agregar un mensaje
```py
message = Text(app, text="Welcome to the Hello world app!")
```
Un salto de línea
```py
objText1 = Text(app, text="\n\n")
```

Ejemplo en guizero
```py
#widgets
ibjText01 = Text(app, text="Control de alumnos", size=40, font="Times new roman", color='#ffffff')
objText2 = Text(app, text="\n")

objText3 = Text(app, text="Introducir su nombre", size=20, font="Times new roman", color='#ffffff')

objTextBox4 = TextBox(app)

objButton5 = PushButton(app, command=say_my_name, text="Mostrar Nombre)
objText6 = Text(app, text="\n")
objText7 = Text(app, text="Resultado", size=20, font="Times new roman", color='#ffffff')

#widgets

app.display()
```

# Crear un espcio en blanco
```py
some_empty_space = Text(app, text="   ", grid=[0,2], align="left")
```

```


```




## tkinter
```py
from datetime import datetime
import tkinter as tk
```

## pywhatkit
Con esta libreria se hacen dibujos en codigo ascci, hay arte de este tipo, se toma una imagen y se convierte a arte ascci

para instalar la herramienta:

``
pip install pywharkit
``

modo de uso
proyecto python
imagen.png
__init__.py

En el archivo __init__, se le dice que imoprte la libreria
```py
import pywhatkit
```

Luego se llama a la libreria y acceder al metodo image to ascci, por defecto el formato de salida es .txt
```py
pywhatkit.image_to_ascii_art("imagen.png", "NombreArchivoFinaldeSalida")
leerArchivo = open("image.png")
print(leerArchivo.read())
```

luego se imprime la variable
```py
leerArchivo = open("imagen.png")
print(leerArchivo.read())
```

## asccii-magic
```py
from ascci_magic import AssciiArt
my_art = AsciiArt.from_image(.png)
my_art.to_html_file('ascii_art.html', columns=200, width_ratio=2)
my_art.to_terminal()

```



## Leer archivos .csv
```py
import pandas as pd
titanic = pd.read_csv(data/data.csv)
print(titanic)

#Leer las primeras 8 lineas
print(titanic.head(8))
#Tipos de datos
print(titanic.dtypes)
```
# Para calcular el tiempo

Se crea una variable y se pone la fecha actual con data.now 

```py
objBoton9 = PushButton(objApp, command=timeCalculator.inicioTime, text="Iniciar Tiempo")
objBoton10 = PushButton(objApp, command=timeCalculator.finTime, text="Finalizar Tiempo")

```
