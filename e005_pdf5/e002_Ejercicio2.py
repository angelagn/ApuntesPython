'''2. Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los
años que ha cumplido (desde 1 hasta su edad).'''

edad = int(input("Por favor escriba su edad: \n"))

for i in range(0, edad):
    print(i + 1)
