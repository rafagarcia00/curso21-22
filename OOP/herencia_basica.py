import os
os.system('clear')

class Base():
    datos = []

class Hijo1(Base):
    datos = []
    def __init__(self, elemento):
        self.datos.append(elemento)
    def datos_base(self):
        return super().datos

class Hijo2(Base):
    datos = []
    def __init__(self, elemento):
        self.datos.append(elemento)
    
    def __str__(self) -> str:
        return 'Soy el hijo 1'

h1 = Hijo1('hijo1')
h2 = Hijo2('hijo2')

print(h1.datos_base())
print(h2)

print(h1.datos)
print(h2.datos)