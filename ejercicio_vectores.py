# multiplicar los numeros de las 2 listas y finalmente sumarlos

v1 = [1,2]
v2 = [7,8]
total = 0
for i in range(len(v1)):
    total += v1[i] * v2[i]
print(total)
