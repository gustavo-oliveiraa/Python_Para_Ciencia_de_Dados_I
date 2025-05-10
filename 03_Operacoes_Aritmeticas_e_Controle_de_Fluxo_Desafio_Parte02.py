# -*- coding: utf-8 -*-
"""
Created on Tue May  6 15:22:52 2025

@author: PC
"""

# Desafio Aula 03 de Python (Parte 2)
"""
Faça um loop que conte de 1 até 100, mas para múltiplos de 3 imprima 'Fizz' em vez do número e para múltiplos de 5 imprima 'Buzz'. 
Para números múltiplos de 3 e 5, imprima 'FizzBuzz'.
"""

#for i in range(100): (gambiarra que deu certo)
#    i += 1
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
