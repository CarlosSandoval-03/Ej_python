#!/usr/bin/env python
# -*- coding: utf-8 -*-
#12. Dados los coeficientes de un polinomio de grado dos y un número real, evaluar la derivada del polinomio en ese número.
def ejDoce(a,b,x):
    return "La derivada en el punto",x,"es",(2 * (a * x)) + b

def main():
    coefA = int(input("Ingrese el coeficiente A: "))
    coefB = int(input("Ingrese el coeficiente B: "))
    numero = int(input("Ingrese valor dado a X: "))
    print(ejDoce(coefA,coefB,numero))

if __name__ == "__main__":
    main()