#mathias Rosales 07/04/25
#VIVA EL MAINCRAA

adivinanza = 0
intentos = 5

while adivinanza != 6 and intentos > 0:
    adivinanza = int(input("adivinanza el número: "))
    intentos -=1
if intentos ==0:
    print("te quedaste sin intentos")
else:
    print("adivinaste")