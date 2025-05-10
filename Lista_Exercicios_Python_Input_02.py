# -*- coding: utf-8 -*-
"""
Created on Fri May  9 15:25:16 2025

@author: PC
"""

# Exercício 02 de Python (Word)

"""
2.	Exercício 2
Código base:
# Exemplo 2: Convertendo a entrada para número inteiro
idade = int(input("Digite sua idade: "))
print("Ano que vem você terá", idade + 1, "anos.")

- Modifique o código para receber outro tipo de entrada (ex: número ao invés de texto).
- Qual seria a saída se o usuário digitasse o valor X?
    Altura inválida
- Adicione uma validação para garantir que a entrada seja válida.
- Crie uma nova versão desse código que use pelo menos duas entradas diferentes do usuário.
"""

""" Parte 1
while True:
    altura = input("Digite sua altura seguindo este formato (0.00): ")
    try:
        altura = float(altura)
        print(f'Sua altura é {round(altura, 2)}')
        break
    except ValueError:
        print('Altura inválida')
"""

# Parte 2
while True:
    altura = input("Digite sua altura seguindo este formato (0.00): ")
    
    try:
        altura = float(altura)
    except ValueError:
        print("Altura inválida. Use o formato 0.00, por exemplo: 1.75")
        continue
    
        maioridade = input("Tem menos de 21 anos (S/N): ").strip().upper()
        
        if maioridade == 'S':
            print(f'Sua altura é {round(altura, 2)} e você ainda crescerá até os 21 anos')
            break
        elif maioridade == 'N':
            print(f'Sua altura é {round(altura, 2)} e você não crescerá mais')
            break
        else:
            print('Digite uma opção entre S (sim) ou N (não).')
