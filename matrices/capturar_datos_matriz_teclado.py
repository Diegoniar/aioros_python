# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 17:51:29 2020

@author:Diego Niño Arias

Crea un array de 10 posiciones de números con valores pedidos por teclado. 
Muestra por consola el indice y el valor al que corresponde. 
Haz dos métodos, uno para rellenar valores y otro para mostrar.
"""

def rellenar_matriz(matriz, pos):
    for i in range(pos):
        numero=int(input("Introduce un número: "))
        matriz.append(numero)

def imprimir_matriz(matriz):
    con=0
    for i in matriz:
        print("Índice [",con,"]:", matriz[i])
        con+=1   
         
posiciones=10
matriz=[]
rellenar_matriz(matriz,posiciones)
imprimir_matriz(matriz)



