from constantes_parking import PRECIO_DIAS, PRECIO_SEMANAS , SEMANA 

def importe(dias):

# 1.- calcular las semanas
    semanas = dias // SEMANA 
# 2.- calcular los dias restantes
    dias_restantes = dias % SEMANA
# 3.- coste por semanas
    coste_semanal = semanas * PRECIO_SEMANAS
# 4.- coste por dias
    coste_dias = dias_restantes * PRECIO_DIAS
# 5.- cálculo del total
    total = coste_dias + coste_semanal

    return total

print(importe(1))