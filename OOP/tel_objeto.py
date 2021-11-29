

import os
os.system('clear')

class movil():
    Marca = None
    Modelo = None
    Color = None
    Alto = None
    Ancho = None
    Peso = None
    Sistema_op = None
    Camara = None


    def encender(self):
        pass
    def apagar(self):
        pass    
    def reiniciar(self):
        pass
    def modo_avion(self):
        pass
    def llamar(self):
        pass
    def recibir_llamadas(self):
        pass

    def __init__(self,marca,modelo,col,alt,anch,peso,sist,cam):
        self.Marca = marca
        self.Modelo = modelo
        self.Color = col
        self.Alto = alt
        self.Ancho = anch
        self.Peso = peso       
        self.Sistema_op = sist
        self.Camara = cam


    def __str__(self) -> str:
        return f'Marca: {self.Marca}\nmodelo: {self.Modelo}\nColor: {self.color}'

    def encender(self):
        self.movil_en_marcha = True
    def apagar(self):
        self.movil_en_marcha = False





redmi = movil('1234-kll',3,'Azul')
redmi.encender
print('motor: ', (redmi.movil_en_marcha))

redmi.Color = 'azul'
redmi.Marca = 'Xiaomi'
redmi.num_puertas = 2
redmi.precio = 20000
redmi.marca = 'BMW'
redmi.modelo = 'Panda'




print(movil.color)
print(movil.num_puertas)
print(movil.matricula)
print(movil.precio)
# pprint.pprint(dir(bmw.__class__))
# pprint.pprint(dir(bmw.__dict__))
print(bmw)
bmw.apagar()
print('motor: ', (bmw.movil_en_marcha))

