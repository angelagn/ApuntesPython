'''Traducir o convertir tipos de variables'''

entero = 50
flotante1 = float(entero)
print(flotante1)

entero2 = int(flotante1)
print(entero2)
#int to string
print(str(entero2))
 #str to int
cadena = "1000"
print(int(cadena))
#Convierte la cadena a entero y suma uno
print(int(cadena)+1)

cadena2 = (int(cadena) + 1)
print(cadena2)
#Averiguar el tipo
print(type(cadena2))
#print(int(cadena + 1))  #Error
#Separar caracteres
deletrear= "Estamos dominando python"
#Deletrear tupla
val1 = tuple(deletrear)
print(val1)
#Deletrear lista
print(list(deletrear))
#Acceder a cada caracter
print(deletrear[0])
print(deletrear[1])


