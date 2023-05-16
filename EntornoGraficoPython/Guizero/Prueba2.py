from guizero import App, Text, Combo, CheckBox, Threading

#grid rejilla para ir posicionanado las cosas en la ventana

app = App(title="App principal", width="800", height="800", bg="red")
#widgets
film_description = Text(app, text="Selecciona Pelicula", grid=[0,0], align="left")
film_choice = Combo(app, options=["Star Wars", "Frozen", "Lion KIngg"], grid=[1,0], align="left")

# #Check box para seleccionar opciones en una caja
#grid=[2,0] el primer indice representa la columna y el segundo la fila
objCheckbox = CheckBox(app, text="Asiento VIP",  grid=[2,0], align="left")
#COntar segundos
#paso 1 import threading

def f():
    print("Hola mundo")

t = Threading.Timer(3, f) # 3 segundos a esperar y la f es la funcion
#t = threading.Timer(10, f2) # 10 segundos a esperar y la f2 es otra funcion
t.start() # para iniciar 
print("Esto se ejecuta antes que la funcion")

app.display()
# def funcionAejecutar():
#     print("hola")

# while True:
#     funcionAejecutar()
#     Time.sleep(1) #espera 1 segundo
#     print("Se ejecuta todo")



