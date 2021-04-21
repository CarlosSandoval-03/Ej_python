#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Ej23 import meterNumeros
#26. Desarrollar un algoritmo que calcule el mı́nimo de un arreglo de números enteros (reales).
def ejVeinteSeis(arreglo):
    x = arreglo[0]
    for i in arreglo:
        if i <= x:
            x = i
    return "El valor minimo es:",x

def main():
    x = []
    meterNumeros(x)
    print(ejVeinteSeis(x))
    
if __name__ == "__main__":
    main()