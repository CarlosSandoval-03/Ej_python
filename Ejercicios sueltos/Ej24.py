#24. Desarrollar un algoritmo que calcule el promedio de un arreglo de enteros (reales).
def suma(arreglo):
    n = len(arreglo)
    if n == 1:
        print(arreglo)
    else:
        suma = 0
        for i in arreglo:
            suma = suma + i
    return suma

def meterNumeros(arreglo):
    a = input("Ingrese numero a insertar en el arreglo (Finalice secuencia con '#'): ")
    if a != "#":
        a = int(a)
        arreglo.append(a)
        meterNumeros(arreglo) 

def ejVeinteCuatro(arreglo):
    n = len(arreglo)
    total = suma(arreglo)
    total /= n
    print("El promedio del arreglo es:",total)
    
def main():
    x = []
    meterNumeros(x)
    ejVeinteCuatro(x)
    
if __name__ == "__main__":
    main()