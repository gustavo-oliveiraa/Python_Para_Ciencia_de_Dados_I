# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""

# Desafio Aula 01 de Python
"""
Crie um script que:
    Peça ao usuário seu nome e idade usando input().
    Converta a idade para inteiro e calcule o ano em que a pessoa nasceu (considerando o ano atual como 2025).
    Mostre uma mensagem formatada com o nome, idade e ano de nascimento.
"""

nome = input("Digite seu nome: ")
idade = input("Digite sua idede: ")

idade_inteiro = int(idade)

ano_nascimento = 2025 - idade_inteiro

print(f'Muito prazer {nome}, sua idade é {idade} e o ano de seu nascimento foi em {ano_nascimento}!')
