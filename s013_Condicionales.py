nombre = "angela"
print("valor", nombre)

edad = 50

if edad > 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

nota1 = 9
if nota1 < 5:
    print("Es menor que 5 ")
elif nota1 < 10:
    print("Es menor que 10 ")
else:
    print("Es mayor o igual que 10")

val1 = 4
val2 = 2

if val2 != 0:
    print(val1/val2)

#if anidado
temperature = 28
if temperature < 20:
    if temperature < 10:
        print("Nivel azul")
    else:
        print("Nivel verde")
else:
    if temperature < 30:
        print("Nivel naranja")
    else:
        print("Nivel rojo")
    
#Expresiones
value = 8

if value != 8:
    print("false")

#Doble consicion
x1 = 8
if x1 > 4 or x1 < 12:
    print("...")


value3 = 99
if value3 is not None:
    print(f'valor {value3}')

#Identidicar direccion de memoria en la que se guarda una variable
val4 = 5
print(id(val4))

#While
#para hacer un contador
valor1 = 0
while (valor1 < 5):
    print(f'valor es {valor1}')
    valor1 += 1

#Poder salir o no de una aplicacióng
# exit = 'N'
# preguntasexamen = 0
# while exit == 'N':
#     print("Bienvenido a la aplicación")
#     exit = input('quieres salir de la aplicación?')
#     preguntasexamen += 1
#     if preguntasexamen == 4:
#         print("maximo numero de preguntas alcanzado")
#         break
# print("bye bye...")

 
#For
#Deletrear con un for
word = "Python"
for letter in word:
    print(letter)

#IMprime hasta la letra que yo quiera 

for letter2 in word:
    if letter2 == 't':
            break
    print(letter2)

#Imprimir numeros del 1 al 20
for i in range(0, 21):
    print(i)

#Imprimir numeros del 1 al 20 de dos en dos
for i in range(0, 21, 2): #El ultimo dos indica cada cuanto
    print(i)

#Imprimir numeros impares del 1 al 20 de dos en dos
for i in range(1, 20, 2): #El ultimo dos indica cada cuanto
    print(i)


for i in range(10, -1, -1): #del 10 al cero restando de uno en uno
    print(i)

#Repetir sentencia muchas veces
#sin definir la variable
for _ in range(10):
    print("hola")

#Bucles anidados
#TABLAS DE MULTIPLICAR
#sacar todas las tablas de multiplicar hasta el 10
'''Los bucles anidados se suelen usar en los arrays bidimensionales'''
for i in range(1, 10): #cada tabla
    for j in range(1, 10): #10 veces para construir la tabla
        result = i * j
        print(f'{i}*{j} = {result}')


#For anidado para matriz de tres dimensiones
# for x in range(1,3):
#     for y in range(1,3):
#         for z in range(1,3):



#creo una funcion que recorre la lista 
def imprimir(animales):
    for animal in animales:
        if animal == "jirafa":
            print(animal)
        else:
            print("No hay jirafa")
#creo una lista
animales = ["perro", "gato", "caballo", "conejo", "jirafa"]

#llamo a la función
imprimir(animales)


#Averiguar si un numero es par o impar
x8 = 6
if not x8%2:
    print("Es par")
else:
    print("es impar")


