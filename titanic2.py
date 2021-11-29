# contar hombres y mujeres vivos y muertos

import os
import csv
import pprint


os.system('clear')
ruta = '/home/rafa/codigo/curso21-22/csv/'

# 1 leer diccionario
def leer_dict():
    csv_in = open('/home/rafa/codigo/curso21-22/csv/titanic.csv') 
    lector_dict = csv.DictReader(csv_in)

    lista_dict = list(lector_dict)

    csv_in.close()
    return lista_dict

def procesar_csv():
    pasajeros = leer_dict()
    mujeres = []
    hombres = []
    h_v = 0
    h_m = 0
    m_v = 0
    m_m = 0
    for p in pasajeros:
        if p ['Sex'] == 'male' and p['Survived'] == '1':
            h_v += 1
        if p ['Sex'] == 'male' and not p['Survived'] == '1':
            h_m += 1    
        if p ['Sex'] == 'female' and p['Survived'] == '1':
            m_v += 1
        if p ['Sex'] == 'female' and not p['Survived'] == '1':
            m_m += 1    
            hombres.append(p['Survived'])
            mujeres.append(p['Survived'])
            

    return (h_m, h_v, m_v, m_m)
resultado =  procesar_csv()
print(f'hombres vivos: {resultado[1]}, hombres muertos: {resultado[0]}')
print(f'Mujeres vivas: {resultado[2]}, mujeres muertas: {resultado[3]}')