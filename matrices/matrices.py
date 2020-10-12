# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 08:41:33 2020

@author: Diego Niño Arias
"""

mi_matriz=[1,45,89,478,48]
"""En python crear una array es tan simple como 
crear una variable y asignarle entre corchetes [] una serie de datos, 
se le asigna el indice segun el orden que lo coloquen"""

for i in mi_matriz:
  print(i)
  """Aca imprimo la matriz usando el bucle for, donde i valdra 0
  e ira aumentando su valor en 1 hasta que llegue al limite del tamaño de 
  la matriz -1"""

mi_matriz[3]=521
"""En este caso modifique el indice 3 (478) por el valor 521"""

mi_matriz.append(20)
mi_matriz.pop(1)
"""Agregue un elemento mas al array y este sera colocado
al final de la lista"""

print("La lista modificada quedaría asi: ")

for i in mi_matriz:
  print(i)

