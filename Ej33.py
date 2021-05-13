from Ej30 import nuevoMeterNumeros
from Ej8 import mcdDosValores
# Hacer un algoritmo que calcule el Maximo Comun Divisor (MCD) para un arreglo de enteros positivos.
# Ejemplo.
#Arreglo: (12,20,14,124,72,2458)
# MCD del arreglo: 2


def mcdArreglo(arreglo):
    num1 = arreglo[0]
    num2 = arreglo[1]
    mcd = mcdDosValores(num1, num2)
    for i in range(2, len(arreglo)):
        mcd = mcdDosValores(mcd, arreglo[i])
    return mcd


def main():
    lista = nuevoMeterNumeros()
    print("El maximo comun divisor de", lista, "es", mcdArreglo(lista))


if __name__ == "__main__":
    main()
