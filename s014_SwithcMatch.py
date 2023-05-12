#Switch de python match

age = 21

match age:
    case 0 | None:
        print("not a person")
    case 10:
        print("menor")
    case 21:
        print("Mayor")


# import random

# dado1 = random.randint(1,6)
# dado2 = random.randint(1,6)

# suma = dado1 + dado2
# print("El primer dado vale: ", dado1)
# print("El segundo dado vale: ", dado2)
# print("La suma dado: ", suma)

# if suma == 9:
#     print("has ganado")
# else:
#     print("has perdido")


'''ESCAPE el slash invertido Escapa el movimiento que se va a hacer despues
da continuidad a la linea para interpretarla como 1
scape, te libra del movimiento que vas a realizar justo despues'''

x = 1.1 + 2.2 \
   +3.3
print(x)

#Otra version del juego de dados importando solo el randint

from random import randint
dado1 = randint(1,6)
dado2 = randint(1,6)

suma = dado1 + dado2

print("El primer dado vale: ", dado1)
print("El segundo dado vale: ", dado2)
print("La suma dado: ", suma)

if suma == 7:
    print("has ganado")
else:
    print("has perdido")