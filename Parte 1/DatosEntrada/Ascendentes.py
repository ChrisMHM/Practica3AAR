import sys

def mejorCaso(n):
    datos = []
    for i in range(1, n+1):
        datos.append(i)
    return datos


def escribeArchivo(file, lista):
    f = open (file, "w")
    for e in lista:
        f.write("%d\n" % e)

    f.close()

def main():
    elementos = (int)(sys.argv[1])
    lista = mejorCaso(elementos)
    nameFile = "ascendente_" + str(elementos) + ".txt"
    escribeArchivo(nameFile, lista)

if __name__== "__main__":
    main()
