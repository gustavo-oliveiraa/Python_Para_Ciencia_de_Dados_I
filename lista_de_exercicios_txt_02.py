# -*- coding: utf-8 -*-
"""
Created on Wed May  7 12:37:15 2025

@author: PC
"""

# Lista de exercícios txt

"""
2. Crie uma função que receba uma frase, e tambem que receba uma palavra.
retorne a frase substituindo a palavra por "****" e print a frase.
"""

def manipular_frase(frase, palavra):
    return frase.replace(palavra, "****")

frase = input("Digite uma frase qualquer:\n")
palavra = input('Digite a palavra que quer substituir por "****":\n')


print(manipular_frase(frase, palavra))
