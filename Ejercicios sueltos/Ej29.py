#29. Desarrollar un algoritmo que determine la mediana de un arreglo de enteros (reales). La mediana es el número que queda en la mitad del arreglo después de ser
#ordenado.
def ejVeinteNueve(arreglo):
    n = len(arreglo)
    arreglo.sort() # Organiza en orden de menor a mayor
    if n%2 == 0:
        n /= 2
        total = (arreglo[int(n-1)] + arreglo[int(n)]) / 2
        print("La mediana del arreglo:",arreglo,"es:",total)
    elif n%2 != 0:
        n /= 2
        n = round(n)
        print("La mediana del arreglo:",arreglo,"es:",arreglo[n])

def meterNumeros(arreglo):
    a = input("Ingrese numero a insertar en el arreglo (Finalice secuencia con '#'): ")
    if a != "#":
        a = int(a)
        arreglo.append(a)
        meterNumeros(arreglo) 

def main():
    x = []
    meterNumeros(x)
    ejVeinteNueve(x)
    
if __name__ == "__main__":
    main()