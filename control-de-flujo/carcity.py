#Mathias Rosales 03/04/25

altura =int(input("Cual es tu altura? (cm) : "))
#crearon una variable para solicitar información al usuario
creditos =int(input("Cuantos creditos tienes? : "))


if altura >= 137 and creditos >=10 :
    print("disfruta tu viaje")
elif altura < 137 and creditos >=10:
    print("no tienes la altura suficiente para subir")
elif creditos < 10 and altura >= 137:
    print("no tienes suficientes creditos")
else:
    print("no cumples con los requisitos altura y creditos para subir")

