import os
from settings import RUTA_BASE, CODIGO, MI_CARPETA

os.system('clear')

actual = os.getcwd()
print(actual)

nuevo_dir = os.chdir(RUTA_BASE)
actual = os.getcwd()
print(actual)
print('-'*50)
archivos = os.scandir(RUTA_BASE + CODIGO)
for a in archivos:
    if a.is_file():
        print(a.name)

ruta_salida = RUTA_BASE + CODIGO + MI_CARPETA
if not os.path.exists(ruta_salida):
    os.makedirs(ruta_salida)


nuevo = open(ruta_salida + '/mi_archivo.txt','w')
nuevo.write('hola mundo')
nuevo.close()
print()