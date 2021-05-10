from Ej22 import criba
from Ej27 import maximoArreglo
# Hacer un algoritmo que calcule el M´ınimo Com´un M´ultiplo (MCM) para un arreglo de enteros positivos.
# Ejemplo.
#Arreglo: (12,20,30,15)


def cuentaArreglo(arreglo, buscar):
    veces = 0
    for elemento in arreglo:
        if elemento == buscar:
            veces += 1
    return veces


def indiceArreglo(arreglo, buscar):
    i = -1
    for elemento in arreglo:
        if elemento != buscar:
            i += 1
        else:
            i += 1
            break
    return i


def arregloEntero(arreglo):
    lista = []
    for elemento in arreglo:
        try:
            elemento1 = int(elemento)
            lista.append(elemento1)
        except:
            elemento1 = round(elemento)
            lista.append(elemento1)
    return lista


def simplificarEnPrimos(arreglo) -> int:
    lista = []
    primos = criba(maximoArreglo(arregloEntero(arreglo)))
    for numero in arreglo:
        for divisores in primos:
            while numero % divisores == 0:
                lista.append(divisores)
                numero /= divisores
        lista.append("|")
    return lista


def mcm(arreglo):
    booleanoCiclo = True
    arregloSimple = simplificarEnPrimos(arreglo)
    while booleanoCiclo:
        for i in range(: arregloSimple):
            pass
    return arregloSimple


def main():
    print(mcm([10, 20]))


if __name__ == "__main__":
    main()
