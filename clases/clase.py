class Personaje:
    def __init__ (self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida
    def atributos (self):
        print(self.__nombre, ":", sep="")
        print("Fuerza:", self.__fuerza)
        print("Inteligencia:", self.__inteligencia)
        print("Defensa:", self.__defensa)
        print("Vida:", self.__vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa

    def esta_vivo(self):
        return self.__vida > 0

    def morir(self):
        self.__vida = 0
        print(self.__nombre, "ha muerto.")

    def daño (self, enemigo):
        return self.__fuerza - enemigo.__defensa

    def atacar (self, enemigo):
        daño = self.daño(enemigo)
        enemigo.__vida = enemigo.__vida - daño
        print(self.__nombre, "ha realizado", daño, "puntos de daño a", enemigo.__nombre)
        if enemigo.esta_vivo():
            print("La vida de", enemigo.__nombre, "es", enemigo.__vida)
        else:
            enemigo.morir()

    def get_fuerza(self):
        return self.fuerza

    def set_fuerza(self, fuerza):
        if fuerza < 0:
            print("Error, has introducido un valor negativo")
        self.fuerza = fuerza


class Guerrero(Personaje):
    def __init__ (self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
    def cambiar_arma(self):
        opcion = int(input("¿Qué espada deseas usar? (1) Acero Valyrio, daño 8 (2) Matadragones daño 10:"))
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10

    def atributos (self):
        super().atributos()
        print("Espada:", self.espada)
        self.cambiar_arma()
        print("Espada:", self.espada)

    def daño (self, enemigo):
        return self.__fuerza * self.espada - enemigo.defensa


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print("Libro: ", self.libro)

    def daño (self, enemigo):
        return self.__inteligencia * self.libro - enemigo.defensa


kaldrogo = Guerrero("Kaldrogo", 20, 30, 20, 100, 5)
mi_personaje = Personaje("Math1.611", 10, 20, 10, 100)
gandalf = Mago("Gandalf", 20, 30, 20, 100, 5)

kaldrogo.atributos()
print("_______________________")
mi_personaje.atributos()
print("_______________________")
gandalf.atributos()
print("_______________________")









# print(kaldrogo.cambiar_arma())
# kaldrogo.atributos()
# print(kaldrogo.espada)



# mi_personaje = Personaje("Math1.611", 10, 20, 10, 100)
# mi_enemigo = Personaje("Juanito", 5, 10, 5, 5)

#print(mi_personaje.get_fuerza())
#mi_personaje.atributos()

