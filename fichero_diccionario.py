import os
import pprint

os.system('clear')

ruta = '/home/rafa/codigo/curso21-22/viernes/programacion/python/lista.py.txt'
dic_salida = {}
clave = 0
# leer archivo
with open(ruta) as archivo:
    for l in archivo:
        # procesar fila a fila
        fila = l[:-1:].split(',')
        # recorrer lista y llenar diccionario
        for nombre in fila:
            dic_salida[nombre] = nombre
            clave += 1

def modo2():
    clave = 0
    texto = open(ruta,'r').readline()
    for archivo in texto:
        dic_salida(clave) = archivo
        clave += 1
    return dic_salida

pprint.pprint

modo2()