# Video 9 : Time: 1:11:40
from Ej35a42 import limpiarConsola
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
    # 44. Sumar: Calcula el polinomio suma y lo imprime.
    # 45. Resta: Calcula el polinomio resta y lo imprime.
    # 46. Multiplicar: Calcula el polinomio multiplicacion y lo imprime.
    # 47. Dividir: Calcula el polinomio division del primer polinomio por el segundo y lo imprime.
    # 48. Residuo: Calcula el polinomio residuo de la division del primero por el segundo y lo imprime.
    # 49. Salir: Permite salir de la aplicacion al usuario.
    # Despues de realizada la operacion el menu se debe presentar de nuevo hasta que el usuario desee salir.


def main():
    limpiarConsola()
    print(polinomio('-3x^2-12x+8.1'))


if __name__ == '__main__':
    main()
