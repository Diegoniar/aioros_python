# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 09:48:54 2020

@author: Diego Niño Arias

Crea un array de caracteres que contenga de la ‘A’ a la ‘Z’ 
 (solo las mayúsculas). Después, ve pidiendo posiciones del array por teclado 
 y si la posicion es correcta, se añadira a una cadena que se mostrara al 
 final, se dejará de insertar cuando se introduzca un -1.

Por ejemplo, si escribo los siguientes numeros
0 //Añadira la ‘A’
5 //Añadira la ‘F’
25 //Añadira la ‘Z’
50 //Error, inserte otro numero
-1 //fin

Cadena resultante: AFZ
"""

alfabeto=('A','B','C','D','E','F','G','H','I','J','K','L','M',
            'N','O','P','Q','R','S','T','U','V','W','X','Y','Z');

x=True;
        
while x:
    pos=int(input("Digite cual posición de la matriz o presione -1 para terminar: "))
    if pos != -1:
        if pos<26:
            print(alfabeto[pos])
        else:
            print("Error, inserte otro número")
                
            
    else:
        x=False;
           
        
        