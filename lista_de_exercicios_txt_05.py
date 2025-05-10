# -*- coding: utf-8 -*-
"""
Created on Wed May  7 15:37:25 2025

@author: PC
"""

# Lista de exercícios txt

"""
5. Crie uma função que recebe um número representando a idade e recebe outro parametro que vai ser um booleano (True ou False).
se ele tiver mais de 18 anos e o booleano for True, retorne "Maior de idade e pode dirigir".
caso ele tenha mais de 18 anos e o booleano for False, retorne "Maior de idade e não pode dirigir".
caso ele tenha menos de 18 anos e o booleano for True, retorne "Menor de idade e a carteira é falsa".
caso ele tenha menos de 18 anos e o booleano for False, retorne "Menor de idade e não pode dirigir".
"""

def verifica_piloto(idade, booleano):
    try:
        idade = int(idade)
        booleano = booleano.strip().upper()
        
        if booleano == 'S':
            booleano = True
        elif booleano == 'N':
            booleano = False
        else:
            return 'Erro: informe apenas S (sim) ou N (não) para a carteira de habilitação.'
            
        if idade >= 18 and booleano == True:
            return 'Maior de idade e pode dirigir'
        elif idade >= 18 and booleano == False:
            return 'Maior de idade e não pode dirigir'
        elif idade < 18 and booleano == True:
            return 'Menor de idade e a carteira é falsa'
        elif idade < 18 and booleano == False:
            return 'Menor de idade e não pode dirigir'
    except ValueError:
        return 'Erro: valores atribuidos errados'
    
idade = input('Digite a idade para verificarmos:\n')
booleano = input('O condutor possui carteira de habilitação (S/N):\n')

print(verifica_piloto(idade, booleano))