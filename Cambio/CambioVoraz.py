#La funcion regresa el total de monedas que se devuelven
def cambioVoraz(montoTotal, denominacion):
    total = 0
    for i in denominacion:
        if i <= montoTotal:
            cantidad = int(montoTotal/i)
            if(cantidad >= 1):
                #print("La cantidad de monedas de " +str(i) +" es: "+str(cantidad))
                total += cantidad
            else:
                #print("No hay solucion")
                pass
            montoTotal = montoTotal%i
    return total

denominacion = [100, 25, 10, 5, 1]
resultado1 = cambioVoraz(8, denominacion)
resultado2 = cambioVoraz(25, denominacion)
resultado3 = cambioVoraz(47, denominacion)
resultado4 = cambioVoraz(642, denominacion)
resultado5 = cambioVoraz(1025, denominacion)
resultado6 = cambioVoraz(356, denominacion)

print("Primer rango de valores")
print("Para 8 se necesitan %d monedas" %resultado1)
print("Para 25 se necesitan %d monedas" %resultado2)
print("Para 47 se necesitan %d monedas" %resultado3)
print("Para 642 se necesitan %d monedas" %resultado4)
print("Para 1025 se necesitan %d monedas" %resultado5)
print("Para 356 se necesitan %d monedas" %resultado6)

denominacion = [6, 4, 1]
resultado1 = cambioVoraz(8, denominacion)
resultado2 = cambioVoraz(25, denominacion)
resultado3 = cambioVoraz(47, denominacion)
resultado4 = cambioVoraz(642, denominacion)
resultado5 = cambioVoraz(1025, denominacion)
resultado6 = cambioVoraz(356, denominacion)

print("Segundo rango de valores")
print("Para 8 se necesitan %d monedas" %resultado1)
print("Para 25 se necesitan %d monedas" %resultado2)
print("Para 47 se necesitan %d monedas" %resultado3)
print("Para 642 se necesitan %d monedas" %resultado4)
print("Para 1025 se necesitan %d monedas" %resultado5)
print("Para 356 se necesitan %d monedas" %resultado6)