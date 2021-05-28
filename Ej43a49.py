from Ej35a42 import limpiarConsola
from metodosTemp import inversoArreglo, maximoArreglo
from metodosTemp import metodoIndex
from Ej35a42 import verificionNoRepeticion


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


def ubicarPolinomios(listaTerminos: list, exponentes: list) -> list:
    listaUbicacion = ['0.0' for i in range(maximoArreglo(exponentes) + 1)]
    temp1 = inversoArreglo(listaTerminos)
    for k in range(len(temp1)):
        listaUbicacion[k] = temp1[k]
    return lista_textoPolinomio(inversoArreglo(listaUbicacion))


def lista_textoPolinomio(lista: list) -> str:
    pos = 0
    listaFinal = []
    for elemento in lista:
        if elemento != '0.0':
            if pos > 0 and pos != 1:
                listaFinal.append(elemento + 'x^' + str(pos))
            elif pos > 0 and pos == 1:
                listaFinal.append(elemento + 'x')
            else:
                listaFinal.append(elemento)
        pos += 1

    temp = ''
    for i in inversoArreglo(listaFinal):
        temp += i
    return temp


def multiplicarPolinomios(polinomio1: list, polinomio2: list) -> list:
    multiplicar = []
    expo = []
    for i in range(len(polinomio1)):
        for k in range(len(polinomio2)):
            temp = polinomio1[i] * polinomio2[k]
            if temp > 0:
                multiplicar.append('+' + str(temp))
                expo.append(i+k)
            elif temp != 0:
                expo.append(i+k)
                multiplicar.append(str(temp))

    counts = {}
    for j in range(len(expo)):
        counts[expo[j]] = counts.get(expo[j], 0) + 1

    copiaMultiplicar = multiplicar.copy()
    operar = []
    listaTemporal = []
    for k, v in counts.items():
        if v > 1:
            for i in range(v):
                index = metodoIndex(expo, k)
                operar.append(copiaMultiplicar[index])  # Debo retornar copia
                copiaMultiplicar.pop(index)
                listaTemporal.append(index)

    sumaTemp = 0
    for h in range(len(operar)):
        sumaTemp += float(operar[h])
        if sumaTemp > 0:
            suma = '+' + str(sumaTemp)
        else:
            suma = str(sumaTemp)
    copiaMultiplicar.insert(listaTemporal[0], suma)
    return ubicarPolinomios(copiaMultiplicar, verificionNoRepeticion(expo))

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
