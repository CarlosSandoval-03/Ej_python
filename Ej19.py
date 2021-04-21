#!/usr/bin/env python
# -*- coding: utf-8 -*-
#19. Si en la UN están podando árboles y cada rama tiene P hojas, y a cada árbol le quitaron K ramas, cuántos árboles se deben podar para obtener T hojas?.
def ejDiezNueve(p,k,t):
    p = int(p)
    k = int(k)
    t = int(t)
    return "El total de arboles es:",(t / (p * k))
    
def main():
    hojas = input("Cuantas hojas hay por rama?: ")
    ramas = input("Cuantas ramas hay por arbol?: ")
    total = input("Cuantas hojas quieres obtener?: ")
    print(ejDiezNueve(hojas,ramas,total))

if __name__ == "__main__":
    main()