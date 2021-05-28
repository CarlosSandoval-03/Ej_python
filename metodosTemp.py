def metodoIndex(element, seeker) -> int:
    count = 0
    for parts in element:
        if parts == seeker:
            return count
        else:
            count += 1
    return -1


def metodoSplit(string: str, separador=" ") -> list:
    listOfTerms = []
    temp = ""
    for element in string:
        if element != separador:
            temp += element
        else:
            listOfTerms.append(temp)
            temp = ""
    if len(temp) > 0:
        listOfTerms.append(temp)
    return listOfTerms


def maximoArreglo(arreglo):
    x = arreglo[0]
    for i in arreglo:
        if i >= x:
            x = i
    return x


def minimoArreglo(arreglo):
    x = arreglo[0]
    for i in arreglo:
        if i <= x:
            x = i
    return x


def inversoArreglo(arreglo: list) -> list:
    temp = []
    n = len(arreglo)
    for i in range(n-1, -1, -1):
        temp.append(arreglo[i])
    return temp


def inSimple(seeker, arreglo):
    boolean = False
    for elemento in arreglo:
        if elemento == seeker:
            boolean = True
    return boolean
