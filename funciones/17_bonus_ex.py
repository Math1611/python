## Mathias Rosales 28/04/25
# no se nada de python ;v

def pedir_numero():
    while True:
        try:
            numero = int(input("Escribe un número entero: "))
            print("Gracias, tu numero es:", numero)
            break
        except ValueError:
            print("Eso no es un número válido. Inténtalo de nuevo.")
pedir_numero()