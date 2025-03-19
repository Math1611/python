tareas = ["Sacar dinero del banco", 
          "hacer la colada", 
          "dar un paseo", 
          "cortarse el cabello",
          "preparar el te",
          "Terminar el capítulo de Listas",
          "llamar a mamá",
          "Ver mi héroe academía"]


print(tareas[0])
print(tareas[1])


tareas_seguidas = tareas[2:5]

print(tareas_seguidas)

try:
    error = tareas[8]
except IndexError as e:
    print(f"Error detectado -> {e}")

tareas += ["ver dc.house"]
print(tareas)