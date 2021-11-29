# contar hombres y mujeres vivos y muertos

import os
import csv


os.system('clear')
ruta = '/home/rafa/codigo/curso21-22/csv/'

# 1 leer diccionario
def leer_dict():
    csv_in = open('/home/rafa/codigo/curso21-22/csv/titanic.csv') 
    lector_dict = csv.DictReader(csv_in)

    lista_dict = list(lector_dict)

    csv_in.close()
    return lista_dict


pasajeros = leer_dict()
def imprimir():
    for i in pasajeros:
        if i['Age'] >= '20' and i['Age'] <= '30' and i['Survived'] == '1': 
            print(i['Name'])
            print(i['Pclass'])
            print(i['Sex'])
        else:
            pass

    return
        
imprimir()
