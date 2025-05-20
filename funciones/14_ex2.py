#mathias Rosales 28/04/25
# no se nada de python ;v

def division_segura():
    try:
        num1 = int(input("ingresa un numero: "))
        num2 = int(input("ingresa otro numero: "))
        resultado = num1 / num2
        print("El resultado de la division es:", resultado)
    except ZeroDivisionError:
        print("Lo sentimos no se puede realizar esta división")
    except ValueError:
        print("Error: solo debes ingresar numeros")
        
division_segura()
