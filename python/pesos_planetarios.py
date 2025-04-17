#Mathias Rosales 09/04/25
#ayuda no sé mucho sobre python ;v

peso_terrestre = float(input("Ingrese el peso terrestre: "))
numero_de_planetas = int(input("Ingrese el número de planeta donde se encuentra (1)Mercurio , (2)Venus , (3)Marte: , (4)Jupiter , (5)Saturno , (6)Urano , (7)Neptuno: "))

destino_peso = peso_terrestre * numero_de_planetas

gravedades = {
    1: 0.38,
    2: 0.91,
    3: 0.38,
    4: 2.34,
    5: 1.06,
    6: 0.92,
    7: 1.19
}

if numero_de_planetas == 1:
    destino_peso = peso_terrestre * gravedades[1]
    print("El peso en Mercurio es: ", destino_peso, "kg")
elif numero_de_planetas == 2:
    destino_peso = peso_terrestre * gravedades[2]
    print("El peso en Venus es: ", destino_peso, "kg")
elif numero_de_planetas == 3:
    destino_peso = peso_terrestre * gravedades[3]
    print("El peso en Marte es: ", destino_peso, "kg")
elif numero_de_planetas == 4:
    destino_peso = peso_terrestre * gravedades[4]
    print("El peso en Jupiter es: ", destino_peso, "kg")
elif numero_de_planetas == 5:
    destino_peso = peso_terrestre * gravedades[5]
    print("El peso en Saturno es: ", destino_peso, "kg")
elif numero_de_planetas == 6:
    destino_peso = peso_terrestre * gravedades[6]
    print("El peso en Urano es: ", destino_peso, "kg")
elif numero_de_planetas == 7:
    destino_peso = peso_terrestre * gravedades[7]
    print("El peso en Neptuno es: ", destino_peso, "kg")
else:
    print("planeta desconocido.")
