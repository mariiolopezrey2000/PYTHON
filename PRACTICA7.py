class agenda:
    def menu(self):
        self.opcion=0
        self.nombre=[]
        self.telefono=[]
        self.correo=[]
        while self.opcion !=5:
            self.opcion = int(input("1-->Cargar contacto\n2-->Listar\n3-->Consultar contacto\n4-->Modificar telefono y correo\n5-->Finalizar "))
            if self.opcion ==1:
                self.alta()
            elif self.opcion ==2:
                self.listar()
            elif self.opcion ==3:
                self.mostrar()                                    
            elif self.opcion ==4:
                self.modificar()
            elif self.opcion ==5:
                self.salir() 
    def alta(self):
        self.nombre.append(input("nombre : "))
        self.telefono.append(int(input("numero de telefono : ")))
        self.correo.append(input("nombre de correo : "))
    def listar(self):
        print("Listado de agenda: ")
        for i in range (len(self.nombre)):
            print(self.nombre[i]," ",self.telefono[i]," ",self.correo[i])
            print(" ")
        
    def mostrar(self):
        nombre=input("Escribe el nombre de la persona que quiere ver ")
        for i in range (len(self.nombre)):
            if self.nombre[i]==nombre:
                print(self.nombre[i]," ",self.telefono[i]," ",self.correo[i])
    def modificar(self):
        nombre=input("Escribe el nombre de la persona que quiere modificar ")
        for i in range (len(self.nombre)):
            if self.nombre[i]==nombre:
                self.telefono[i]=int(input("Escribe el nuevo numero de telefono " ))
                self.correo[i]=input("Escribe el nuevo correo ")
    def salir(self):
        print("Ha salido del programa")
#bloque principal
Agenda=agenda()
Agenda.menu()