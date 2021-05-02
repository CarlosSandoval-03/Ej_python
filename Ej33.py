from Ej30 import nuevoMeterNumeros
from Ej22 import criba #Lista Criba
from Ej27 import maximoArreglo #Mayor Numero
#Hacer un algoritmo que calcule el Maximo Comun Divisor (MCD) para un arreglo de enteros positivos.
#Ejemplo.
#Arreglo: (12,20,14,124,72,2458)
#MCD del arreglo: 2
def mcd(arreglo) -> list:
    for elemento in arreglo:
        listaPrimos = criba(maximoArreglo(elemento)) #Lista de primos hasta mayor numero del arreglo
        for numerosPrimos in listaPrimos:
            


def main():
    lista = nuevoMeterNumeros()
    print(lista)
if __name__ == "__main__":
    main()
