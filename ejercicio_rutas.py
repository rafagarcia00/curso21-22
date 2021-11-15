# import os
# from route import RUTA_BASE, CODIGO, MI_CARPETA

# os.system('clear')


# # crear archivo
# nuevo_dir = os.chdir(RUTA_BASE)
# actual = os.getcwd()
# print(actual)
# print('-'*5)
# # buscar archivos
# archivos = os.scandir(RUTA_BASE + CODIGO)
# for a in archivos:
#     if a.is_file():
#         print(a.name)

# ruta_salida = RUTA_BASE + CODIGO + MI_CARPETA
# if not os.path.exists(ruta_salida):
#     os.makedirs(ruta_salida)

# nuevo = open(ruta_salida + '/mi_archivo.txt','w')
# nuevo.write('hola mundo')
# nuevo.close()
# print()

# # guardar los archivos de 5 en 5





import os
from posixpath import join 
import settings

os.system('clear')

lista_archivo = []
archivo_salida = settings.RUTA_BASE + settings.CODIGO + settings.MI_CARPETA
ruta_salida = settings.RUTA_BASE + settings.CODIGO + settings.MI_CARPETA
miembros = 5
fila = ''
# Buscar los archivos
archivo = os.scandir(settings.RUTA_BASE + settings.CODIGO)
for a in archivo:
    if a.name.endswith('.py'):
    # if not a.is_dir() and not a.name.startswith('.'):
        lista_archivo.append(a.name[:-3:])
# Agruparlos de 5 en 5 
for i in range(0,len(lista_archivo),miembros):
    temp = lista_archivo[i: i + miembros]
    fila += ','.join(temp) + '\n'

# Guardar archivos en el fichero
nuevo = open(ruta_salida + '/lista.txt','w')
nuevo.write(fila)
nuevo.close()
# Seleccionar los archivos

# Procesar nombre de archivos