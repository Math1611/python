#mathias Rosalesa 14/04/25
# # #ayuda no sé mucho sobre python ;v

import random

palabras_fortuna = [
    "No persigas la felicidad, créala.",
    "Todas las cosas son difíciles antes de ser fáciles.",
    "El pajaro madrugador consigue el gusano, pero el segundo ratón se lleva el queso.",
    "Alguien en tu vida necesita una carta de tu parte.",
    "No solo pienses. ¡Actúa!.",
    "TU corazon se acelerará.",
    "La fortuna que buscas está en otra galleta.",
    "Ayuda! Estoy prisionero en una panaderia china!."
]

def fortuna():
    fortuna = random.randint(0, len(palabras_fortuna) - 1)
    print(palabras_fortuna[fortuna])

fortuna()
fortuna()
fortuna()
