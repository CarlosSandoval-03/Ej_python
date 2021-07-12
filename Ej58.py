from metodosTemp import limpiarConsola, leer_matriz_enteros

def eliminar(a, b, col, target=0):
    fac = (b[col] - target) / a[col]
    for i in range(len(b)):
        b[i] -= fac * a[i]

def gauss(matriz):
    for i in range(len(matriz)):
        if matriz[i][i] == 0:
            for j in range(i + 1, len(matriz)):
                if matriz[i][j] != 0:
                    matriz[i], matriz[j] = matriz[j], matriz[i]
                    break
            else:
                return None
        for j in range(i + 1, len(matriz)):
            eliminar(matriz[i], matriz[j], i)
    for i in range(len(matriz)-1, -1, -1):
        for j in range(i - 1, -1, -1):
            eliminar(matriz[i], matriz[j], i)
    for i in range(len(matriz)):
        eliminar(matriz[i], matriz[i], i, target = 1)
    return matriz

def inversa(matriz):
    temp = [[] for _ in matriz]
    for i,row in enumerate(matriz):
        assert len(row) == len(matriz)
        temp[i].extend(row + [0] * i + [1] + [0] * (len(matriz)-i-1))
    gauss(temp)
    final = []
    for i in range(len(temp)):
        final.append(temp[i][len(temp[i]) // 2:])
    return final


def main():
    n = int(input('Ingrese numero columnas: '))
    m = int(input('Ingrese numero filas : '))
    matriz = leer_matriz_enteros(n,m)
    print(inversa(matriz))


if __name__ == "__main__":
    main()
