# Mathias Rosales 28/04/25
# no se nada de python ;v

def funcion(a,b,*args, **kwargs):
    print("a=", a)
    print("b=", b)
    for arg in args:
        print("args=", arg)
    for key, value in kwargs.items():
        print(key, "=", value)
    
funcion(1,2,3,4,5,6,7,8,9,10, nombre="Luis", edad=25)

