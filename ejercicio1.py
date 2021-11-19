import os
import pprint

os.system('clear')

def introduce():
    personas = {}
    

    for i in range(10):
        nombre = input("introduzca nombre: ")
        apellidos = input("introduzca apelidos: ")
        dni = input("introduzca DNI: ")
        fecha_de_nacimiento = input("introduzca la fecha de nacimiento: ")
        telefono = input("introduzca su teléfono: ")
        continuar = input("¿Quiere seguir introduciendo datos? (S/N): ")
        personas[dni] = {'nombre':nombre, 'apellidos':apellidos, 'fecha': fecha_de_nacimiento, 'teléfono': telefono, 'DNI': dni}

        if continuar == 'S':
            pass
        elif continuar == 'N':
            break

    return personas

pprint.pprint(introduce()) 
