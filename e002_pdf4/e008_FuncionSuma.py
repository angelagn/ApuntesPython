'''8. Crear una funcion de suma con 3 parámetros, uno sin valor y los otros 2 con valores por defecto. Nos
devolverá la suma de los 3 parámetros
- Probar la funcion con un parametro
- Probar la función con 2 parametros
- Guardar en una variable la funcion ( s = suma )
- Utilizar la funcion como objeto ( result1 = s(8,8) )
- Imprimir el result1
Puede tener como referencia el siguiente ejemplo de 2 parámetros'''
 
def suma(a, b=7, c = 8):
    return a+b+c
print("el resultado de la suma es", suma(3))
print("EL resultado es: ", suma(4, 6))

s = suma
resultado = s(8,8)
print(resultado)