# -*- coding: utf-8 -*-
"""
Created on Tue May  6 15:45:13 2025

@author: PC
"""

# Desafio Aula 04 de Python
"""
Crie uma função chamada calcular_media que receba 3 números e retorne a média deles.
Depois, crie uma função lambda que, dado um número, diga se ele está acima da média, na média, ou abaixo da média, considerando a média calculada.
"""

def calcular_media(num1, num2, num3):
    return (num1 + num2 + num3) / 3

num1 = float(input("Digite a primeira nota para tirar a média: "))
num2 = float(input("Digite a segunda nota para tirar a média: "))
num3 = float(input("Digite a terceira nota para tirar a média: "))

media = calcular_media(num1, num2, num3)

nivel_media = lambda nota: "Acima da Média" if nota > media else ( "Na Média" if nota == media else "Abaixo da Média")

nota = float(input("Digite a nota para ver se está na média tirada a pouco: "))

print(nivel_media(nota))
    