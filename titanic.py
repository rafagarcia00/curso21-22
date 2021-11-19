# contar vivos y muertos

import os
import csv

os.system('cls')

ruta = '/home/rafa/codigo/curso21-22/csv/'

# 1 leer diccionario
def leer_archivo():
    csv_in = open(ruta + '/titanic.csv') 
    lector_dic = csv.DictReader(csv_in)

    lista_dict = list(lector_dic)

    csv_in.close()
    return lista_dict
    
# 2 leer survived
def leer_valores():
    survivors = []
    titanic_list = leer_archivo()
    for persona in titanic_list:
        actual_person = persona.values()
        for actual in actual_person:
            survivors = {}
            survivors.append
    return survivors

# 3- contar (0=muerto, 1=vivo)
def contar_vivos_muertos():
    vivo = 0
    muerto = 0
    for number in leer_valores():
        if number == '1':
            vivo += 1
        else:
            muerto += 1
    return vivo, muerto


v,m = contar_vivos_muertos()
print(v)
print(m)