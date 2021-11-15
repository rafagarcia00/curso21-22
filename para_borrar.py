import os
import settings


os.system('clear')

lista_archivo = []
ruta_salida = settings.RUTA_BASE + settings.CODIGO + settings.MI_CARPETA
miembros = 5
fila = ''

def buscar():

    archivo = os.scandir(settings.RUTA_BASE + settings.CODIGO)
    for a in archivo:
        if a.name.endswith('.py'):
            lista_archivo.append(a.name[:-3:])


    ruta_salida = open ('lista.py.txt','r')
    print(ruta_salida)