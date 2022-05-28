class triangulo:
    
    def inicializar(self):
        self.lado1=int(input("Escribe el lado 1"))
        self.lado2=int(input("Escribe el lado 2"))
        self.lado3=int(input("Escribe el lado 3"))
    def imprimir(self):
        mayor=self.lado1
        if mayor> self.lado2 and mayor> self.lado3:
            print ("lado mayor es el lado 1 con un valor de ",self.lado1)
        else:
            if mayor< self.lado2 and self.lado2>self.lado3:
                print ("lado mayor es el lado 2 con un valor de ",self.lado2)
            else: 
                if mayor< self.lado3 and self.lado3>self.lado2:
                    print ("lado mayor es el lado 3 con un valor de ",self.lado3)
                else:
                    print("todos los lados son iguales")
    def equilatero(self):
        if self.lado1==self.lado2 and self.lado1==self.lado3:
            print("el triangulo es equilatero")
        else:
            print("el triangulo no es equilatero")
#bloque principal
triangulo1=triangulo()  
triangulo1.inicializar()
triangulo1.imprimir()
triangulo1.equilatero()