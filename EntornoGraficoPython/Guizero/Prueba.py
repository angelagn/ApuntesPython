#Para ejecutar desde consola se va a la carpeta de ubicación del archivo y se ejecuta:
# python3 Prueba.py

from guizero import App, Text, PushButton, TextBox, PushButton, Picture, Combo, CheckBox
import time #La libreria time se importa por sepadaro
# def funcion1():
#      print("Boton pulsado")
   

#app = App(title="Hello world")
# message = Text(app, text="Welcome to the Hello world app!")
# objText1 = Text(app, text="\n\n")
# objText = Text(app, text="\n\n")
# version = Text(app, text = "version app 2.0")
# objText2 = Text(app, text="\n\n")
# ayuda = Text(app, text="ayuda manual en linnk")
# objText3 = Text(app, text="control de alumnos", size = 20, color="lightblue")
# button1 = PushButton(app, text="Pulsar aqui", command=funcion1) #funcion que quiero #2que ejecute el boton
#Logotipo siempre buscarlo con fondo transparente
#la imagen se pone en el mismo nivel del archivo que estamos programando


#EJEMPLO 2


def say_my_name():
    print("Hola")
    objText8.value = objTextBox5.value

#Funcion para mostrar la hora actual con la libreria time
def counter():
    objText14.value = str(time.strftime("%H:%M:%S")) #24 horas
    print(time.strftime("%I:%M:%S")) #12 horas
    print(time.strftime("%d/%m/%y")) #FOrmato de fecha actual
    

app = App(title="App principal", width="800", height="800", bg="red") #COlor del fondo de la pagina
#widgets
objText01 = Text(app, text="Control de alumnos", size=40, font="Times new roman", color='#ffffff')
objText2 = Text(app, text="\n")

objText3 = Text(app, text="Introducir su nombre", size=20, font="Times new roman", color='#ffffff')

objTextBox5 = TextBox(app)


objButton5 = PushButton(app, command=say_my_name, text="Mostrar Nombre")
objText7 = Text(app, text="\n")
objText8 = Text(app, text="Resultado", size=20, font="Times new roman", color='#ffffff')
objPicture = Picture(app, image="giphy.gif")

#mostrar la hora actual con la funcion time
objText14 = Text(app, text="0")
objText14.repeat(1000, counter)
#Obtener la hora actual
ahora = time.strftime("%c") #FOrmato de fecha actual


#Combo para seleccionar una opcion
objCombo11 = Combo(app, options=["casada", "soltera", "divorciada"])

#Check box para seleccionar opciones en una caja
objCheckbox12 = CheckBox(app, text="Aprobado")
objCheckbox13 = CheckBox(app, text="Suspenso")



#widgets


app.display()

