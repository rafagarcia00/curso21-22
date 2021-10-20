objetivo = 33
veces = 0

for i in range(10):
    veces +=1
    intento = int(input("introduce un número: "))
if objetivo > intento:
        print("Es mayor")
elif objetivo < intento:
        print("Es menor")
else:
    print(f"Has acertado en {veces} intentos")
    break
if veces > 9:
    print(f"Has perdido.\n El número era (objetivo)")