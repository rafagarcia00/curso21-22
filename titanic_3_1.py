import os
import csv

os.system('clear')
ruta = '/home/rafa/codigo/curso21-22/csv/'

def leer_dict():
    csv_in = open('/home/rafa/codigo/curso21-22/csv/titanic.csv') 
    lector_dict = csv.DictReader(csv_in)

    lista_dict = list(lector_dict)

    csv_in.close()

    return lista_dict


pasajeros = leer_dict()
def imprimir():
    hay_cabecera = False
    for i in pasajeros:
        if i['Age'] >= '20' and i['Age'] <= '30' and i['Survived'] == '1': 
            with open(ruta + 'titanic_nombres.csv','a') as csv_writer:
                escribir = csv.writer(csv_writer)
                if not hay_cabecera:

                    escribir.writerow(['Nombre','Clase','Sexo'])            
                    hay_cabecera = True
                else:
                    escribir.writerow([i['Name'], i['Pclass'], i['Sex']])
        

    return
        
imprimir()
