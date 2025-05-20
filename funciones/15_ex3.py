# Mathias Rosales 28/04/25
# no se nada de python ;v

def mostrar_elemento():
    frutas = ["manzana", "banana", "naranja", "uva"]
    try:
        indice = int(input(" elige una posición (0-3): "))
        print("fruta elegida", frutas[indice]) 
    except IndexError:
        print("Esta posición no existe en la lista")
    except ValueError:
        print("Debes ingresar un número")

mostrar_elemento()