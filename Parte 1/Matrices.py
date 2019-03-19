
def cambio(monedas, monto):
    maximo = monto + 1
    tabla = [maximo]*maximo
    tabla[0] = 0

    for i in range(1, monto):
        for j in range(len(monedas)-1):
            if monedas[j] <= i:
                tabla[i] = min(tabla[i], tabla[i - monedas[j]] + 1)
    
    print(tabla)
    return -1 if tabla[monto] > monto else tabla[monto]

monedas = [1, 6, 4]
resultado = cambio(monedas, 8)
print(resultado)

