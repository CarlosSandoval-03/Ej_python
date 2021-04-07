#28. Desarrollar un algoritmo que calcule el producto directo de dos arreglos de enteros (reales) de igual tamaño. Sean v = (v 1 , v 2 , . . . , v n ) y 
# w = (w 1 , w 2 , . . . , w n ) dos arreglos, el producto directo de v y w (notado v ∗ w) es el vector: (v 1 ∗ w 1 , v 2 ∗ w 2 , . . . , v n ∗ w n ).
def ejVeinteOcho(arreglo1,arreglo2):
    n1 = len(arreglo1)
    n2 = len(arreglo2)
    if n1 == n2:
        productoDirecto = []
        for i in range(n1):
            resultado = arreglo1[i] * arreglo2[i]
            productoDirecto.append(resultado)
        print("El producto directo de los dos arreglos es:",productoDirecto)
    else:
        print("Los arreglos no son del mismo tamaño")

def meterNumeros(arreglo):
    a = input("Ingrese numero a insertar en el arreglo (Finalice secuencia con '#'): ")
    if a != "#":
        a = int(a)
        arreglo.append(a)
        meterNumeros(arreglo) 
 
def main():
    x = []
    y = []
    meterNumeros(x)
    meterNumeros(y)
    ejVeinteOcho(x,y)
    
if __name__ == "__main__":
    main()