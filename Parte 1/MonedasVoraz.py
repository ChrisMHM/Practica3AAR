monedas = [700, 6, 4, 1]
def DevolverCambio(dinero, monedas):
    for i in monedas:
        if i <= dinero:
            cantidad = int(dinero/i)
            if(cantidad >= 1):
                print("La cantidad de monedas de " +str(i) +" es: "+str(cantidad))
            else:
                print("No hay solucion")
            dinero = dinero%i

dinero = int(input("Ingrese la cantidad: "))
DevolverCambio(dinero, monedas)