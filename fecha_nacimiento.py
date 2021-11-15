def nacimiento():
    meses = (1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre')
    fecha = input('Dime cuando naciste (dd/mm/aaaa): ')
    partes = fecha.split('/')
    mes = int(partes[1]) -1
    mensaje = 'Naciste el día ' + partes[0] + ' del mes ' + meses[int(partes[1])] + ' del año ' + partes[2]
    return mensaje

print(nacimiento())