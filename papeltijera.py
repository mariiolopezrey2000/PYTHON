from random import random
class jugador:
    def __init__(self):
        self.eleccion1 = input("Elige piedra, papel o tijera: ")
        
class maquina:
    def __init__(self):
        lista=["piedra","papel","tijera"]
        self.eleccion = lista[int(random()*3)]

class juego:
    puntuacionjugador=0
    puntuacionmaquina=0
    def __init__(self):
        while self.puntuacionjugador <3 and self.puntuacionmaquina <3:
            self.eleccionjugador = jugador()
            self.eleccionmaquina = maquina()
            self.resultado()
        if self.puntuacionjugador > self.puntuacionmaquina:
            print("Has ganado")
        else:
            print("Has perdido")
    def resultado(self):
        print("Elegiste: ",self.eleccionjugador.eleccion1)
        print("La maquina eligio: ",self.eleccionmaquina.eleccion)
        if self.eleccionjugador.eleccion1 == self.eleccionmaquina.eleccion:
            print("Empate")
        elif self.eleccionjugador.eleccion1 == "piedra" and self.eleccionmaquina.eleccion == "tijera":
            print("Ganaste")
            self.puntuacionjugador+=1
        elif self.eleccionjugador.eleccion1 == "papel" and self.eleccionmaquina.eleccion == "piedra":
            print("Ganaste")
            self.puntuacionjugador+=1
        elif self.eleccionjugador.eleccion1 == "tijera" and self.eleccionmaquina.eleccion == "papel":
            print("Ganaste")
            self.puntuacionjugador+=1
        elif self.eleccionjugador.eleccion1 == "piedra" and self.eleccionmaquina.eleccion == "papel":
            print("Perdiste")
            self.puntuacionmaquina+=1
        elif self.eleccionjugador.eleccion1 == "papel" and self.eleccionmaquina.eleccion == "tijera":
            print("Perdiste")
            self.puntuacionmaquina+=1
        elif self.eleccionjugador.eleccion1 == "tijera" and self.eleccionmaquina.eleccion == "piedra":
            print("Perdiste")
            self.puntuacionmaquina+=1
        print("Puntuacion jugador: ",self.puntuacionjugador)
        print("Puntuacion maquina: ",self.puntuacionmaquina)
#bloque principal
juego = juego()