# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 21:18:02 2020

@author: Diego Niño Arias
"""
import random as r

def es_primo(numero):
    aux=0
    for i in range(numero):
        if numero%(i+1) == 0:
            aux+=1
    return aux<3

def llenar_matriz(matrix,pos):
    i=0
    aux=0
    while i<pos:
        aux=r.randint(1, 1000)
        if es_primo(aux):
            matrix.append(aux)
            i+=1
            
def mostrar_contenido(matrix):
    j=0
    for i in matrix:
        print("Posición[",j,"]=",i)
        j+=1

def mayor(matrix):
    aux=0
    for i in matrix:
        if i>aux:
            aux=i
    print("El número mayor es: ",aux)
    
posiciones=int(input("Cuantos posiciones quiere para la matriz: "))
matriz=[]
llenar_matriz(matriz, posiciones)
mostrar_contenido(matriz)
mayor(matriz)
