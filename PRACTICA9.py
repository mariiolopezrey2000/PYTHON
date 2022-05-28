def cargar():
    i=0
    personas={}
    while i<4:
        nombre=input("Ingrese nombre:")
        dni=input("Ingrese DNI:")
        personas[dni]=nombre
        i+=1
    return personas
def imprimir(personas):
    print("personas:")
    for dni in personas:
        print(dni," ",personas[dni])
def consultar_por_numero(personas):
    dni=input("Ingrese DNI a consultar:")
    if dni in personas:
        print("El nombre es:",personas[dni])
    else:
        print("No existe el DNI")

# bloque principal
personas=cargar()
imprimir(personas)
consultar_por_numero(personas)

