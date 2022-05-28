import random

class dados:
    def tirar(self):
        self.valor=random.randint(1, 6)
    def mostrar(self):
        print("El valor del dado es: ",self.valor)
    def retornar(self):
        return self.valor
    
class jugardados:
    def __init__(self):
        self.dado1=dados()
        self.dado2=dados()
        self.dado3=dados()
    
    def juego(self):
        self.dado1.tirar()
        self.dado2.tirar()
        self.dado3.tirar()
        self.dado1.mostrar()
        self.dado2.mostrar()
        self.dado3.mostrar()
        if self.dado1.retornar()==self.dado2.retornar() and self.dado2.retornar()==self.dado3.retornar():
            print("Ganaste")
        else:
            print("Perdiste")
            
# bloque principal
j= jugardados()
j.juego()