# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""

# Exercício 01 de Python (Word)

"""
1.	Exercício 1
Código base:
# Exemplo 1: Entrada simples de texto
nome = input("Digite seu nome: ")
print("Olá,", nome)

- Modifique o código para receber outro tipo de entrada (ex: número ao invés de texto).
- Qual seria a saída se o usuário digitasse o valor X?
- Adicione uma validação para garantir que a entrada seja válida.
- Crie uma nova versão desse código que use pelo menos duas entradas diferentes do usuário.

"""

""" Parte 1
while True:
    numero = input('Digite um número: ')
    try: 
        numero = float(numero)
        print(f'O número digitado foi {numero}')
        break
    except ValueError:
        print('Porfavor digite um número')
"""   

# Parte 2

while True:
    nome = input('Digite seu nome: ')
    idade = input('Digite sua idade: ')
    
    if not nome.isalpha():
        print('Porfavor digite um nome válido (apenas letras).')
        continue
    
    try:
        idade = int(idade)
        print(f'Olá {nome}, você possui {idade} anos e ano que vem ou nesse ano fara {idade + 1}!')
        break
    except ValueError:
        print('Por favor, digite uma idade válida (número).')