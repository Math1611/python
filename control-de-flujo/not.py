#Mathias Rosales 02/04/25
#cuando me quedo solo en casa hago guturales

respuesta = input("Estas cansado? (Si/No):").strip().lower()

cansado = respuesta == "si"

if not cansado: 
    print("Es hora de programar")
else:
    print("tomate un descanso")