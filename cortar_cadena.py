cadena = 'uno, dos, tres, cuatro, cinco, seis, siete'
inicio = 0
trozo = ''
resultado = []
num_comas = cadena.count(',') +1

for i in range(num_comas):
    final = cadena.find(',',inicio)
    if final == -1:
        trozo = cadena[inicio:]
    else:
        trozo = cadena[inicio:final]
        resultado.append(trozo.strip())
    inicio = final + 1

print(resultado)

# a = []
# for x in cadena:
#     a.append(cadena[:4:22])
#     break
# print(a)





# a=[]
# a.append("uno", )
# a.append("dos", )
# a.append("tres", )
# a.append("cuatro", )
# a.append("cinco", )
# print(a)




# lista = cadena.split(',')
# print(lista)


# resultado esperado ['uno', 'dos'...]