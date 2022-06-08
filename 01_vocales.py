'''
Programa que pide caracteres e imprime 'VOCAL' si son vocales y 'NO VOCAL' en caso contrario, 
el programa termina cuando se introduce un espacio
'''

def letra():
    seguir = True

    while seguir:
        vocal = input('introduce una letra: ')

        if vocal.upper() == 'A' or vocal.upper() == 'E' or vocal.upper() == 'I' or vocal.upper() == 'O' or vocal.upper() == 'U':
            print('VOCAL')
        elif vocal == ' ':
            return 'fin del bucle'
        else:
            print('NO VOCAL')

print(letra()) 
