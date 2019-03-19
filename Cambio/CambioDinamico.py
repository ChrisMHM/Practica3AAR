#La funcion devuelve el monto minimo de monedas
def cambioDinamico(montoTotal, denominacion):
    N = montoTotal + 1
    n = len(denominacion)
    tabla = [[1 for c in range(N)] for f in range(n)]

    for i in range(n):
        tabla[i][0] = 0

    for i in range(n):
        for j in range(N):
            if i == 0 and j < denominacion[i]:
                tabla[i][j] = 0
            elif i == 0:
                tabla[i][j] = 1 + tabla[0][j - denominacion[0]]
            elif j < denominacion[i]:
                tabla[i][j] = tabla[i-1][j]
            else:
                tabla[i][j] = min(tabla[i-1][j], 1 + tabla[i][j - denominacion[i]])

    return tabla[i][j]


denominacion = [1, 5, 10, 25, 100]
tabla1 = cambioDinamico(8, denominacion)
tabla2 = cambioDinamico(25, denominacion)
tabla3 = cambioDinamico(47, denominacion)
tabla4 = cambioDinamico(642, denominacion)
tabla5 = cambioDinamico(1025, denominacion)
tabla6 = cambioDinamico(356, denominacion)

print("Primer rango de valores")
print("Para 8 se necesitan %d monedas" %tabla1)
print("Para 25 se necesitan %d monedas" %tabla2)
print("Para 47 se necesitan %d monedas" %tabla3)
print("Para 642 se necesitan %d monedas" %tabla4)
print("Para 1025 se necesitan %d monedas" %tabla5)
print("Para 356 se necesitan %d monedas" %tabla6)

denominacion = [1, 4, 6]
tabla7 = cambioDinamico(8, denominacion)
tabla8 = cambioDinamico(25, denominacion)
tabla9 = cambioDinamico(47, denominacion)
tabla10 = cambioDinamico(642, denominacion)
tabla11 = cambioDinamico(1025, denominacion)
tabla12 = cambioDinamico(356, denominacion)

print("Segundo rango de valores")
print("Para 8 se necesitan %d monedas" %tabla7)
print("Para 25 se necesitan %d monedas" %tabla8)
print("Para 47 se necesitan %d monedas" %tabla9)
print("Para 642 se necesitan %d monedas" %tabla10)
print("Para 1025 se necesitan %d monedas" %tabla11)
print("Para 356 se necesitan %d monedas" %tabla12)