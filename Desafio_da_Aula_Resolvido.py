# -*- coding: utf-8 -*-
"""
Created on Tue May  6 15:47:29 2025

@author: PC
"""

# Desafio Final da Aula
"""
🧠 Desafio Final: Cadastro de 3 Alunos com Análise de Notas
💼 Contexto
Você precisa desenvolver um programa simples para uma escola fictícia, que receberá dados de 3 alunos, suas notas, e imprimirá a situação de cada um com base na média. 
Caso ele fique de recuperação, quero que ele tenha a opção de fazer a prova de recuperação, e troque a pior nota dele, e recalcule a media.


📋 Requisitos
Cadastrar 3 alunos:

Nome do aluno

Nota 1, Nota 2 e Nota 3

Calcular a média

Exibir resultado formatado com:

Nome em letras maiúsculas

Média

Situação:

Aprovado (média ≥ 7)

Recuperação (5 ≤ média < 7)

Reprovado (média < 5)
"""

print("-" * 10, " Cadastros dos Alunos ", "-" * 10)

aluno1, aluno2, aluno3 = input("Digite os nomes dos 3 aluno separada por virgula:\n").split(",")

aluno1_nota1, aluno1_nota2, aluno1_nota3 = input(f'Digite as 3 notas do {aluno1} (aluno 1) separado por virgula:\n').split(",")
aluno2_nota1, aluno2_nota2, aluno2_nota3 = input(f'Digite as 3 notas do {aluno2} (aluno 2) separado por virgula:\n').split(",")
aluno3_nota1, aluno3_nota2, aluno3_nota3 = input(f'Digite as 3 notas do {aluno3} (aluno 3) separado por virgula:\n').split(",")

def calcular_media(nota1, nota2, nota3):
    return (float(nota1) + float(nota2) + float(nota3)) / 3

def avaliar_aluno(aluno, nota1, nota2, nota3):
    media = calcular_media(nota1, nota2, nota3)
    if media >= 7:
        return f'{aluno.upper()} aprovado com média {round(media, 2)}'
    elif  5 <= media < 7:
        print(f'Aluno {aluno.upper()} está de recuperação com média {round(media, 2)}')
        return recuperacao(aluno, nota1, nota2, nota3)
    else:
        return f'{aluno.upper()} reprovado com média {round(media, 2)}'

def recuperacao(aluno, nota1, nota2, nota3):
    nota_recuperacao = input(f'Digite a nota de recuperação do {aluno.upper()}: ')
    if nota1 < nota2 and nota1 < nota3:
        media = (float(nota2) + float(nota3) + float(nota_recuperacao)) / 3
    elif nota2 < nota1 and nota2 < nota3:
        media = (float(nota1) + float(nota3) + float(nota_recuperacao)) / 3
    elif nota3 < nota1 and nota3 < nota2:
        media = (float(nota1) + float(nota2) + float(nota_recuperacao)) / 3
    elif nota1 == nota2 == nota3:
        
    else:
        media = (float(nota1) + float(nota2) + float(nota3)) / 3

    if media >= 7:
        return print(f'{aluno.upper()} aprovado com média {round(media, 2)}')
    else:
        return print(f'{aluno.upper()} reprovado com média {round(media, 2)}')
    
print(avaliar_aluno(aluno1, aluno1_nota1, aluno1_nota2, aluno1_nota3))
print(avaliar_aluno(aluno2, aluno2_nota1, aluno2_nota2, aluno2_nota3))
print(avaliar_aluno(aluno3, aluno3_nota1, aluno3_nota2, aluno3_nota3))