#Mathias Rosales 09/04/25
#ayuda no sé mucho sobre python ;v

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

# Pregunta 1
respuesta1 = int(input("\n¿Te gusta más el amanecer o el atardecer? (1)amanecer (2)atardecer : "))

if respuesta1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif respuesta1 == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Entrada incorrecta.")

# Pregunta 2
respuesta2 = int(input("\nCuando muera, quiero que la gente me recuerde como: (1) El bueno , (2) El grandioso , (3) El sabio , (4) El valiente : "))

if respuesta2 == 1:
    hufflepuff += 2
elif respuesta2 == 2:
    slytherin += 2
elif respuesta2 == 3:
    ravenclaw += 2
elif respuesta2 == 4:
    gryffindor += 2
else:
    print("Entrada incorrecta.")

# Pregunta 3
respuesta3 = int(input("\n¿Qué tipo de instrumento complace más a tu oído? (1) Violín , (2) trompeta , (3) piano , (4) Tambor : "))

if respuesta3 == 1:
    slytherin += 4
elif respuesta3 == 2:
    hufflepuff += 4
elif respuesta3 == 3:
    ravenclaw += 4
elif respuesta3 == 4:
    gryffindor += 4
else:
    print("Entrada incorrecta.")

# Mostrar resultados
print("\n--- Puntajes finales ---\n")
print("Gryffindor:", gryffindor)
print("Ravenclaw:", ravenclaw)
print("Hufflepuff:", hufflepuff)
print("Slytherin:", slytherin)

#bonus 


casa = ""
mayor = 0

if gryffindor > mayor:
    casa = "Gryffindor"
    mayor = gryffindor
if ravenclaw > mayor:
    casa = "Ravenclaw"
    mayor = ravenclaw
if hufflepuff > mayor:
    casa = "Hufflepuff"
    mayor = hufflepuff
if slytherin > mayor:
    casa = "Slytherin"
    mayor = slytherin

print("\n¡El Sombrero Seleccionador ha decidido que vas a", casa + "!")
print("Felicidades!!!!")
