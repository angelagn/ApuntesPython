from guizero import App, Text, PushButton
def funcion1():
    print("Boton pulsado")
   

app = App(title="Hello world")
message = Text(app, text="Welcome to the Hello world app!")
version = Text(app, text = "version app 2.0")
ayuda = Text(app, text="ayuda manual en linnk")
button1 = PushButton(app, text="Pulsar aqui", command=funcion1) #funcion que quiero 2que ejecute el boton

app.display()
