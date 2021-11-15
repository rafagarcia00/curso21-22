from pprint import pprint

variable = [('campo1','valor1'),
            ('campo2','valor2'),
            ('campo3','valor3'),
            ('campo1','valor1'),
            ('campo2','valor2'),
            ('campo3','valor3')]

dic = dict(variable)
pprint(dic.items()) 

for k,v in dic.items():
    print(k,v)

# -----------------------
claves = dic.keys
valores = dic.values()
pprint(claves)
pprint(valores)

for c in list(claves):
    print(c)