#Para ejecutar desde consola se va a la carpeta de ubicación del archivo y se ejecuta:
# python3 Prueba.py

from guizero import App, Text, PushButton
def funcion1():
     print("Boton pulsado")
   

app = App(title="Hello world")
message = Text(app, text="Welcome to the Hello world app!")
objText1 = Text(app, text="\n\n")
objText = Text(app, text="\n\n")
version = Text(app, text = "version app 2.0")
objText2 = Text(app, text="\n\n")
ayuda = Text(app, text="ayuda manual en linnk")
objText3 = Text(app, text="control de alumnos", size = 20, color="lightblue")
button1 = PushButton(app, text="Pulsar aqui", command=funcion1) #funcion que quiero #2que ejecute el boton

#Logotipo siempre buscarlo con fondo transparente
#la imagen se pone en el mismo nivel del archivo que estamos programando

app.display()

