cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"},

   {"nombre": "José José", "pais": "Mexico"},

   {"nombre": "Juan Luis Guerra", "pais": "Republica Dominicana"}
]

def iterarDiccionario2(artista, nac):
    for diccionario in artista:
        print(", ".join(f"{key}: {value}" for key, value in diccionario.items()))
    for diccionario in nac:
        print(", ".join(f"{key}: {value}" for key, value in diccionario.items()))



iterarDiccionario2(cantantes)