class operaciones:
    def __init__(self):
        self.nu1 = int(input("Escribe el primer numero"))
        self.nu2 = int(input("Escribe el segundo numero"))
        self.suma()
        self.resta()
        self.multiplicacion()
        self.divisional()
        self.printar()
    def suma(self):
        self.su = self.nu1+self.nu2
    def resta(self):
        self.rest = self.nu1-self.nu2
    def multiplicacion(self):
        self.multi = self.nu1*self.nu2
    def divisional(self):
        self.divi = self.nu1/self.nu2
    def printar(self):
        print("la suma es ",self.su)
        print("la resta es ",self.rest)
        print("la division",self.divi)
        print("la multiplicacion",self.multi)
#bloque principal
operacion1=operaciones()
