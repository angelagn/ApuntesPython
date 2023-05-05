'''5. Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el
número de años, y muestre por pantalla el capital obtenido en la inversión cada año que
dura la inversión'''

cantidad = float(input("Ingrese la cantidad a invertir: "))
interes = float(input("Ingrese el interés anual: "))
anios = int(input("Ingrese el número de años: "))

for i in range(1, anios+1):
    capital = cantidad * (1 + interes/100)**i
    print("Capital obtenido en el año", i, ":", capital)

