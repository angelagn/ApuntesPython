def procesarDivision():
    divisor = int(input("introduce el divisor"))
    obtenerDividendo(divisor)

def obtenerDividendo(divisor):
    dividendo = int(input("intropduce el dividendo"))
    dividir(divisor, dividendo)

def dividir(divisor, dividendo):
    resultado = dividendo / divisor
    print("el resultado de la division es: " + str(resultado))

procesarDivision()