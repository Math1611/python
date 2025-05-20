## Mathias Rosales 28/04/25
# no se nada de python ;v


def buscar_cantante():
    cantantes = {
        "nombre": "Luis Miguel",
        "país" : "mexico",
    }
    try:
        clave = input("¿Que quieres saber? (nombre o país): ")
        print("Resultado:", cantantes[clave])
    except KeyError:
        print("No existe la clave")

buscar_cantante()