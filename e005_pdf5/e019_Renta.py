'''19. Los tramos impositivos para la declaración de la renta en un determinado país son los
siguientes:
Renta Tipo impositivo
Menos de 10000€ 5%
Entre 10000€ y 20000€ 15%
Entre 20000€ y 35000€ 20%
Entre 35000€ y 60000€ 30%
Más de 60000€ 45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo
impositivo que le corresponde'''

print("====================================== \n")
print("Por favor elija su renta anual: \n")
print("1. Menos de 10000 euros")
print("2. Entre 10000 y 20000 euros")
print("3. Entre 20001 y 35000 euros")
print("4. Entre 35002 y 60000 euros")
print("5. Más de 60000 euros")
renta  = int(input("Por favor ingrese un número: \n")) 


match renta:
    case 1:
        print("Renta Tipo impositivo 5%")
    case 2:
        print("Renta Tipo impositivo 15%")
    case 3:
        print("Renta Tipo impositivo 20%")
    case 4:
        print("Renta Tipo impositivo 30%")
    case 5:
        print("Renta Tipo impositivo 45%")

