class persona:
    def inicializar(self):
        self.nombre = input("Escribe el nombre de la persona")
        self.edad = int(input("Ingrese la edad: "))
    def comprobar(self):
        if self.edad >=18:
            print(self.nombre,"Es mayor de edad")
        else:
            print(self.nombre,"es menor de edad")

#bloque principal
persona1=persona()
persona1.inicializar()
persona1.comprobar()

