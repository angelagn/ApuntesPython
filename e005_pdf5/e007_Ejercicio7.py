'''7. Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10'''


for i in range(1, 10+1): #cada tabla
    print("Tabla del", i)
    for j in range(1, 10+1): #10 veces para construir la tabla
        result = i * j
        print(f'{i}*{j} = {result}')
