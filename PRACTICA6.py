
class Alumnos:
    def menu(self):
        self.opcion=0
        while self.opcion !=4:
            self.opcion = int(input("1-->alta alumnos\n2-->Listar\n3-->Mostrar alumnos con nota mayor a 7\n4-->Finalizar"))
            if self.opcion ==1:
                self.alta()
            elif self.opcion ==2:
                self.listar()
            elif self.opcion ==3:
                self.mostrar()                                    
            elif self.opcion ==4:
                self.salir()    
    def alta(self):
        self.alum=[]
        self.notas=[]
        for i in range(5):
            self.alum.append(input("nombre de Alumno "))
            self.notas.append(float(input("nota del alumno ")))
    def listar(self):
        print("Listado de alumnos: ")
        for i in range (len(self.alum)):
            print(self.alum[i],self.notas[i])
        
    def mostrar(self):
        print("Listado de alumnos con mas o 7 : ")
        for i in range (len(self.alum)):
            if self.notas[i]>=7:
                print(self.alum[i],self.notas[i])
        
    def salir(self):
        print("Ha salido del programa")
        
#bloque principal
alumnos=Alumnos()
alumnos.menu()