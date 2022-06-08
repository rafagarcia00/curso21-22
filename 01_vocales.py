'''
Programa que pide caracteres e imprime 'VOCAL' si son vocales y 'NO VOCAL' en caso contrario, 
el programa termina cuando se introduce un espacio
'''

def letra():
    seguir = True
    vocal = input('introduce una letra: ')

    while seguir:
        if vocal.upper() == 'A' or vocal.upper() == 'E' or vocal.upper() == 'I' or vocal.upper() == 'O' or vocal.upper() == 'U':
            return 'VOCAL'
        if vocal.upper == ' ':
            return False
        else:
            return 'NO VOCAL'

print(letra()) 
