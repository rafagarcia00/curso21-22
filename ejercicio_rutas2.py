import os
import settings

def clear():
    os.system('clear')




def buscar():
    """
    Busca en la carpeta seleccionada archivos que acaben en .py y la devuelve en una lista sin .py
    """
    lista_archivo = []
    archivo = os.scandir(settings.RUTA_BASE + settings.CODIGO)
    for a in archivo:
        if a.name.endswith('.py'):
            lista_archivo.append(a.name[:-3:])
    return lista_archivo

def agrupar(lista_archivo,miembros):
    """
    Toma una lista de cadenas de texto y devuelve agrupamientos de esas cadenas
    """
    fila = ''
    for i in range(0,len(lista_archivo),miembros):
        temp = lista_archivo[i: i + miembros]
        fila += ','.join(temp) + '\n'
    return fila[:-1]

def escribir(cadena,archivo):
    """
    Recoge la cadena de texto y la guarda en un archibo de texto sustituyendo el contenido del archivo
    """
    nuevo = open(archivo,'w')
    nuevo.write(cadena)
    nuevo.close()
# print(buscar())
x = buscar()
f = agrupar(x,5)
print(f)

ruta = settings.RUTA_BASE + settings.CODIGO
ruta_salida = settings.RUTA_BASE + settings.CODIGO + settings.MI_CARPETA
clear()