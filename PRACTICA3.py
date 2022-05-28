class cuadrado:
    def __init__(self):
        self.lado=float(input("Escribe un numero"))
    def calcular(self):
        self.perimetro=self.lado*4
        self.superficie=self.lado*self.lado
    def printar(self):
        print("el perimetro es de :",self.perimetro)
        print("la superficie es de :",self.superficie)
#bloque
cuadrado1=cuadrado()
cuadrado1.calcular()
cuadrado1.printar()