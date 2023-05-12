# librerías python para entorno grafico

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

## tkinter
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
```

luego se imprime la variable
```py
leerArchivo = open("imagen.png")
print(leerArchivo.read())
```

## asccii-magic
```py
from ascci_magic import AssciiArt
```

my_art = AsciiArt.from_image(.png)
my_art.to_html_file('ascii_art.html', columns=200, width_ratio=2)
my_art.to_terminal()