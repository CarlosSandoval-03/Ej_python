# 27. Desarrollar un algoritmo que calcule el máximo de un arreglo de números enteros (reales).
def ejVeinteSiete(arreglo):
    x = arreglo[0]
    for i in arreglo:
        if i >= x:
            x = i
    print("El valor máximo es:",x)

def meterNumeros(arreglo):
    a = input("Ingrese numero a insertar en el arreglo (Finalice secuencia con '#'): ")
    if a != "#":
        a = int(a)
        arreglo.append(a)
        meterNumeros(arreglo) 

def main():
    x = []
    meterNumeros(x)
    ejVeinteSiete(x)
    
if __name__ == "__main__":
    main()