import sys

def monedas(total, denominacion):
    N = total + 1
    n = len(denominacion)
    tabla = [[1 for c in range(N)] for f in range(n)]
    #print(tabla)
    
    for i in range(n):
        tabla[i][0] = 0

    for i in range(n):
        for j in range(N):
            if i == 0 and j < denominacion[i]:
                tabla[i][j] = 0
                print("Primero tabla[%d][%d] = %d" % (i, j, tabla[i][j]))
            elif i == 0:
                tabla[i][j] = 1 + tabla[0][j - denominacion[0]]
                print("Segundo tabla[%d][%d] = %d" % (i, j, tabla[i][j]))
            elif j < denominacion[i]:
                tabla[i][j] = tabla[i-1][j]
                print("Tercero tabla[%d][%d] = %d" % (i, j, tabla[i][j]))
            else:
                tabla[i][j] = min(tabla[i-1][j], 1 + tabla[i][j - denominacion[i]])
                print("Cuarto tabla[%d][%d] = %d" % (i, j, tabla[i][j]))
                

    return tabla
                
    
denominacion = [2, 4, 6]
tabla = monedas(8, denominacion)
print(tabla)