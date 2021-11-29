from pprint import pprint
import os
import datetime
import csv

from csv_write import csv_write
datetime.date

def pedir_personas ():

    seguir = True
    lista_personas =[]
    while seguir:
        print('introduzca datos. (N para terminar)')

        nombre = input('Nombre: ')
        apellidos = input('Apellidos: ')
        fecha_nac = input('Fecha nacimiento: ')
        telefono = input('Teléfono: ')
        mi_dic = {'nombre': nombre, 'apellidos': apellidos, 'fecha nacimiento': fecha_nac, 'teléfono': telefono}
    
        lista_personas.append(mi_dic)

        respuesta = input('¿Desea continuar s/n: ')
        if respuesta.upper() == 'N': 
            seguir = False
        os.system('clear')
    
    return(lista_personas)

def guardar_csv(contenido, destino):
    with open(destino, 'w', newline='')as f:
            escritor = csv.DictWriter(f, fieldnames=list(contenido[0].keys()))
            escritor.writeheader()
            escritor.writerows(contenido)

cont = pedir_personas()
ruta = '/home/rafa/codigo/curso21-22/csv/personas.csv'

guardar_csv(cont,ruta)