import os

os.system('clear')

class Base():
    __nombre = None
    def __init__(self) -> None:
        self.datos = []

    def set_nombre(self, _mi_nombre):
        self.__nombre = _mi_nombre

    def get_nombre(self):
        return self.__nombre

class Hijo1(Base):
    def __init__(self, elemento):
        super().__init__()
        self.datos.append(elemento)

class Hijo2(Base):
    def __init__(self, elemento):
        super().__init__()
        self.datos.append(elemento)

h1 = Hijo1('hijo1')
h1.nombre = 'Paco'

h2 = Hijo2('hijo2')
h2.nombre = 'Pepe'
print(h1.get_nombre())
print(h2.get_nombre())