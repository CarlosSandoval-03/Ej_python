from Ej35a42 import limpiarConsola
from metodosTemp import maximoArreglo
from metodosTemp import inSimple
from metodosTemp import metodoIndex
from metodosTemp import maximoArreglo

# Metodo Split ------------------------------------


def splitPolinomios(polinomio: str) -> list:
    listOfTerms = []
    temp = ''
    for element in range(len(polinomio)):
        if polinomio[element] == '+' or polinomio[element] == '-':
            listOfTerms.append(temp)
            temp = ''
        temp += polinomio[element]
    listOfTerms.append(temp)
    if listOfTerms[0] == '':
        listOfTerms.pop(0)
    return listOfTerms
# Coeficientes ------------------------------------


def coeficienteSubOperacion(polinomios: int) -> float:
    temp = ''
    i = 0
    while i < (len(polinomios)) and polinomios[i] != 'x':
        temp += polinomios[i]
        i += 1
    return float(temp)


def coeficientes(listaPolinomios: list) -> list:
    listOfCoefficients = []
    for i in range(len(listaPolinomios)):
        listOfCoefficients.append(coeficienteSubOperacion(listaPolinomios[i]))
    return listOfCoefficients
# Exponentes ------------------------------------


def exponenteSubOperacion(listaExponentes: int) -> int:
    n = len(listaExponentes)
    if listaExponentes[n-1] == 'x':
        return 1
    i = 0
    while i < n and listaExponentes[i] != 'x':
        i += 1
    if i == n:
        return 0
    else:
        temp = ''
        for j in range(i+2, n):
            temp += listaExponentes[j]
        return int(temp)


def exponentes(listaPolinomios: list) -> list:
    listOfExponents = []
    for i in range(len(listaPolinomios)):
        listOfExponents.append(exponenteSubOperacion(listaPolinomios[i]))
    return listOfExponents
# Grado ------------------------------------


def maximoGrado(listaExponentes: list) -> int:
    return maximoArreglo(listaExponentes)
# Lista Polinomio ------------------------------------


def meterPolinomios(coeficienteLista: list, exponenteLista: list) -> list:
    m = len(coeficienteLista)
    poliniomio = [0 for i in range(maximoGrado(exponenteLista) + 1)]
    for i in range(m):
        poliniomio[exponenteLista[i]] = coeficienteLista[i]
    return poliniomio

# Un polinomio de grado n, como P(x) = anxn + an−1xn−1 + ⋯ + a1x1 + a0x0 se puede representar mediante un arreglo de reales de la siguiente manera: (a0,a1,...,an−1,an).
# Usando esta representacion hacer un programa que le permita al usuario leer dos polinomios y escoger mediante un menu, una de las siguientes operaciones sobre dichos polinomios:


def polinomio(string: str) -> list:
    temp = splitPolinomios(string)
    expo = exponentes(temp)
    coef = coeficientes(temp)
    return meterPolinomios(coef, expo)
# 43. Evaluar: Lee un real e imprime la evaluacion de los dos polinomios en dicho dato.


def evaluarSimple(polinomio: list, real: float) -> list:
    n = len(polinomio)
    pos = 0
    listaFinal = []
    while pos < n:
        for termino in polinomio:
            listaFinal.append(str(termino) + '(' + str(real ** pos) + ')')
            pos += 1
    return listaFinal


def evaluar(polinomio1: list, polinomio2: list, real: float) -> tuple:
    return (evaluarSimple(polinomio1, real), evaluarSimple(polinomio2, real))
# 44. Sumar: Calcula el polinomio suma y lo imprime.


def sumarPolinomios(polinomio1: list, polinomio2: list) -> list:
    sumar = []
    for i in range(len(polinomio1)):
        temp = polinomio1[i] + polinomio2[i]
        sumar.append(temp)
    return sumar

# 45. Resta: Calcula el polinomio resta y lo imprime.


def restarPolinomios(polinomio1: list, polinomio2: list) -> list:
    restar = []
    for i in range(len(polinomio1)):
        temp = polinomio1[i] - polinomio2[i]
        restar.append(temp)
    return restar
# 46. Multiplicar: Calcula el polinomio multiplicacion y lo imprime.


def igualarArreglos(polinomio1: list, polinomio2: list) -> list:
    n = len(polinomio1)
    m = len(polinomio2)
    a1 = polinomio1.copy()
    a2 = polinomio2.copy()
    if n != m:
        temp = maximoArreglo([n, m])
        if n == temp:
            a2.append(0.0)
        elif m == temp:
            a1.append(0.0)
        return igualarArreglos(a1, a2)
    else:
        return (a1, a2)


def polinomio_diccionario(lista: list) -> dict:
    diccionario = dict()
    pos = 0
    for elemento in lista:
        diccionario[pos] = elemento
        pos += 1
    return diccionario


def multiplicarPolinomios(lista1: list, lista2: list) -> list:
    temp_listas = igualarArreglos(lista1.copy(), lista2.copy())

    polinomio1 = temp_listas[0]
    polinomio2 = temp_listas[1]

    dict_polinomio1 = polinomio_diccionario(polinomio1)
    dict_polinomio2 = polinomio_diccionario(polinomio2)

    i = 0
    dict_polinomioTotal = {}
    while i < len(polinomio2):
        for key, value in dict_polinomio1.items():
            dict_polinomioTotal[key] = [value, polinomio2[i]]
            i += 1

    return dict_polinomio1, dict_polinomio2, dict_polinomioTotal

# 47. Dividir: Calcula el polinomio division del primer polinomio por el segundo y lo imprime.
# 48. Residuo: Calcula el polinomio residuo de la division del primero por el segundo y lo imprime.
# 49. Salir: Permite salir de la aplicacion al usuario.
# Despues de realizada la operacion el menu se debe presentar de nuevo hasta que el usuario desee salir.


def main():
    limpiarConsola()
    # y = polinomio('2x^3+5x-3')
    # z = polinomio('2x^3-3x^2+4x')
    # print(sumarPolinomios(y, z))
    # print(restarPolinomios(y, z))
    a = polinomio('2x^2-3')
    b = polinomio('2x^3-3x^2+4x')
    print(multiplicarPolinomios(a, b))
    print()
    # c = polinomio('2x+1')
    # d = polinomio('1+1x-1x^2')
    # print(multiplicarPolinomios(c, d))


if __name__ == '__main__':
    main()
