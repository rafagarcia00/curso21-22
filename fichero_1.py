from pprint import pprint
archivo = 'listas3.py'
listas = open(archivo)
lineas = listas.readlines()
for l in lineas:
    pprint(l)

listas.close()

# pprint(lineas)
