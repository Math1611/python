#Mathias Rosales 09/04/25
#ayuda no sé mucho sobre python ;v

estaciones = int(input("¿En qué mes del año estamos y te diré la estación que andamos. (1-12): "))

if estaciones  in [1, 2 ,3]:
    print("Invierno")

elif estaciones in [4, 5 ,6]:
    print("Primavera")

elif estaciones in [7, 8 ,9]:
    print("Verano")

elif estaciones in [10, 11 ,12]:
    print("Otoño")

else:
    print("Que dices, este numero no es un mes del año, no sea tonto")

