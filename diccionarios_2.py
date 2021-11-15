import pprint
d = {}
d1 = dict({
    ('clave1', 1),
    ('clave2', 2),
    ('clave3', 3),
    ('clave4', 4)
    })

# crear un diccionario y posteriormente agregarle mas palabras
d1['fruta'] =  ['manzana','pera','uva']
v1 = d1['fruta']
v1.append('platano','sandia')
d1['fruta'] = v1

print(d1['fruta'])
pprint.pprint(d1)

# BORRAR ELEMENTO
del(d1['clave1'])
pprint.pprint(d1)

# Obtener todas las claves

claves = d1.keys()
pprint.pprint(claves)

# obtener todos los valores

valores = d1.values()
pprint.pprint(valores)

# iterar sobre un diccionario

for k in d1:
    print(d1[k])

    for k,v in d1.items():
        print(f'clave: {k} valor: {v}')

# limpiar diccionario

# d1.clear()
# print(d1)

# elementos del diccionario

print(d1.items())

# extraer elementos del diccionario

# elem = d1.pop('fruta')
d1['ultimo'] = 'FIN'
elem = d1.popitem()
print(elem)
print(d1)

