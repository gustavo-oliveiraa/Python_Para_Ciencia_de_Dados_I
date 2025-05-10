# -*- coding: utf-8 -*-
"""
Created on Tue May  6 15:09:20 2025

@author: PC
"""

# Desafio Aula 03 de Python (Parte 1)
"""
Crie um programa que peça um número ao usuário e diga se ele é par ou ímpar.
"""

numero = input("Digite um número e vou te dizer se é par ou ímpar: ")

numero_inteiro = int(numero)

if (numero_inteiro % 2 != 0) :
    print("Ímpar")
else:
    print("Par")
    