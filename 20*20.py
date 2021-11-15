# matriz = ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',]
# for i in range(20):
#     print(matriz)

import pprint
cols = 15
filas = 15
matriz = []

for i in range(filas):
    fila = []
    for i in range(cols):
        fila.append('x')
    matriz.append(fila)

pprint.pprint(matriz)