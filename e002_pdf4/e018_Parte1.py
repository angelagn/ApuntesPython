'''18. Practicaremos un return multiple, guardalo en un modulo, importarlo desde otro modulo y
usarlo'''

def suma_y_media(a, b, c):
    suma = a + b + c
    media = suma / 3
    return suma, media

suma, media = suma_y_media(9, 6, 3)
print(suma)
print(media)