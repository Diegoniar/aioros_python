# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 18:13:53 2020

@author: Diego Niño Arias

Crea un array de números donde le indicamos por teclado el tamaño 
del array, rellenaremos el array con números aleatorios entre 0 y 9, 
al final muestra por pantalla el valor de cada posición y la suma de 
todos los valores. Haz un método para rellenar el array 
(que tenga como parámetros los números entre los que tenga que generar),
para mostrar el contenido y la suma del array y un método privado para
generar número aleatorio (lo puedes usar para otros ejercicios).
"""
import random as r

def __numeroAleatorio():
    return r.randint(0, 9)

def llenar_matriz(matrix,pos):
    for i in range(pos):
        matrix.append(__numeroAleatorio())

def mostrar_contenido(matrix):
    j=0
    for i in matrix:
        print("Posición[",j,"]=",i)
        j+=1

def suma_matriz(matrix):
    suma=0
    for i in matrix:
        suma+=i
    print("La suma de la matriz es: ",suma)

posiciones=int(input("De cuantas posiciones quiera la matriz: "))
matriz=[]
llenar_matriz(matriz, posiciones)
mostrar_contenido(matriz)
suma_matriz(matriz)