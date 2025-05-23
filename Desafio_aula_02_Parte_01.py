# -*- coding: utf-8 -*-
"""
Created on Fri May 23 15:30:08 2025

@author: PC
"""

# Desafio Aula 02

alunos = {}

for i in range(3):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    notas = []
    
    for j in range(3):
        nota = float(input(f"Digite a nota {j+1} de {nome}: "))
        notas.append(nota)

    media = sum(notas) / 3

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
        print(f"\n{nome.upper()} está em recuperação.")
        opcao = input("Deseja fazer a prova de recuperação? (s/n): ").lower()
        if opcao == 's':
            nota_recuperacao = float(input("Digite a nota da prova de recuperação: "))
            pior_nota = min(notas)
            notas[notas.index(pior_nota)] = nota_recuperacao
            media = sum(notas) / 3
            situacao = "Aprovado" if media >= 7 else "Recuperação"
    else:
        situacao = "Reprovado"

    alunos[nome] = {
        "notas": notas,
        "media": round(media, 2),
        "situacao": situacao
    }

print("\n===== RESULTADO FINAL =====")
for nome, dados in alunos.items():
    print(f"Aluno: {nome.upper()}")
    print(f"Média: {dados['media']}")
    print(f"Situação: {dados['situacao']}")
    print("---------------------------")
