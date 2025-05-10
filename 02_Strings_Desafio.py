# -*- coding: utf-8 -*-
"""
Created on Thu May  1 14:31:50 2025

@author: PC
"""

# Desafio Aula 02 de Python
"""
Crie um programa que:
    Solicite ao usuário que insira seu nome e sobrenome em variaveis separadas.
    Mostre o nome completo, com a primeira letra maiúscula e o resto minúscula.
"""

nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")

nome_formatado = nome.capitalize()

sobrenome_formatado = sobrenome.lower()


print(f'Muito prazer {nome_formatado} {sobrenome_formatado}.')
