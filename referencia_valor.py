# def suma(num):
#     num[0] +=12
#     return num

# n = [8]
# print(suma(n))
# print(n)

import random

def genera_equipos(alumnos, miembros=2):
    random.shuffle(alumnos)
    equipos = []

    for i in range(0,len(alumnos),miembros):
        equipos.append(alumnos(i: i + miembros))

    return equipos