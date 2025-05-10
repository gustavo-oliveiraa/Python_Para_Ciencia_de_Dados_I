# -*- coding: utf-8 -*-
"""
Created on Wed May  7 12:44:45 2025

@author: PC
"""

# Lista de exercícios txt

"""
3. Crie uma função que receba uma frase, e tambem que receba uma palavra.
Caso essa palavra esteja na frase, retorne True, caso não esteja, retorne False.
** dica : use o operador "in" para verificar se a palavra está na frase. **
"""

def verificar_palavra(frase, palavra):
    if palavra in frase:
        return True
    else:
        return False
    
frase = input("Digite uma frase:\n")
palavra = input("Digite uma palavra para verificar se ela está na frase:\n")

print(verificar_palavra(frase, palavra))
