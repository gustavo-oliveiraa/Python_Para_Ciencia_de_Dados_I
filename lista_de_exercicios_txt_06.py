# -*- coding: utf-8 -*-
"""
Created on Wed May  7 15:57:10 2025

@author: PC
"""

# Lista de exercícios txt

"""
6. Crie um código de Menu, onde o usuário vai escolher uma opção de 1 a 4.
O código tem que continuar executando enquanto o usuário não escolher a opção 0.
O que deve conter nas opções de 1 a 4 é de escolha do usuário, o principal é que o código continue executando enquanto o usuário não escolher a opção 0.
** dica : utilize o operador "while" para fazer o loop. **
"""
from datetime import datetime
import time

opcao = -1

while opcao != 0:
    print('\nMenu de Opções:')
    print('1 - Ver informações do usuário')
    print('2 - Calcular soma de dois números')
    print('3 - Mostrar data e hora atual')
    print('4 - Exebir uma mensagem motivacional')
    print('0 - Sair')
    
    try:
        opcao = int(input('Digite uma opção de 0 a 4: '))
        
        if opcao == 1:
            print('Usuário: João - Função: Estudante de Python')
            time.sleep(2)
        elif opcao == 2:
            num1 = int(input('Digite o primeiro número: '))
            num2 = int(input('Digite o segundo número: '))
            print(f'Soma: {num1 + num2}')
            time.sleep(2)
        elif opcao == 3:
            agora = datetime.now()
            data_formatada = agora.strftime('%d/%m/%Y %H:%M:%S')
            print(f'Data e hora atual: {data_formatada}')
            time.sleep(2)
        elif opcao == 4:
            print('Você é capaz de conquistar qualquer coisa, continue estudando!')
            time.sleep(2)
        elif opcao == 0:
            print('Obrigado por usar nosso menu. Até logo!')
            time.sleep(2)
        else:
            print('Opção inválida. Tente novamente.')
            time.sleep(2)
    except ValueError:
        print('Por favor, digite um número válido.')
        time.sleep(2)
