file = open("ascendente_"+str(i)+".txt", "r")

for linea in file.readlines():
    print(linea)
file.close()