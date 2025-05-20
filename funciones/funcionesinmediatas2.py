cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"},

   {"nombre": "José José", "pais": "Mexico"},

   {"nombre": "Juan Luis Guerra", "pais": "Republica Dominicana"}
]

def iterarDiccionario(lista):
    for diccionario in lista:
        print(", ".join(f"{key}: {value}" for key, value in diccionario.items()))

iterarDiccionario(cantantes)
