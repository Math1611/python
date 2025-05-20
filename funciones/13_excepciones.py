# Mathias rosales 28/04/2025
# no se nada de python ;v

def pedir_numero():
    try:
        numero = int(input("Introduce un número: "))
        print("Gracias!! Tu numero es:", numero)
    except ValueError:
        print("Eso no es un número válido. Intenta otra vez.")
        
pedir_numero()