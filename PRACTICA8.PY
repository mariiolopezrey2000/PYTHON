def cargar():
    diccionario={}
    continua="si"
    while continua=="si":
        castellano=input("Ingrese palabra en castellano:")
        ingles=input("Ingrese palabra en ingles:")
        diccionario[ingles]=castellano
        continua=input("Quiere cargar mas palabras:[si/no]")
    return diccionario


def imprimir(diccionario):
    print("diccionario:")
    for ingles in diccionario:
        print(ingles,diccionario[ingles])


def consulta_palabra(diccionario):
    palabra=input("Ingrese la palabra en ingles que quiere conocer:")
    if palabra in diccionario:
        print("En castellano significa:",diccionario[palabra])
#BLOQUE PRINCIPAL
diccionario=cargar()
imprimir(diccionario)
consulta_palabra(diccionario)
