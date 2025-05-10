# -*- coding: utf-8 -*-
"""
Created on Wed May  7 12:48:31 2025

@author: PC
"""

# Lista de exercícios txt

"""
4. Crie uma função de calculadora, aonde ela vai receber 2 números, e um operador.
retorne o resultado da operação. Caso seja um operador inválido, retorne "Operador inválido".
** dica : utilize o operador "if, elif e else" para verificar qual operação deve ser feita. **
"""

def calculadora(num1, num2, operador):
    try:
        num1 = float(num1)
        num2 = float(num2)
        
        if operador == '+':
            return num1 + num2
        elif operador == '-':
            return num1 - num2
        elif operador == '*':
            return num1 * num2
        elif operador == '/':
            if num2 == 0:
                return 'Erro: divisão por zero'
            return num1 / num2
        else:
            return 'Operador inválido'
    except ValueError:
        return 'Erro: entrada inválida. Certifique de digitar números'
    
num1 = input('Digite o primeiro número que deseja realizar uma operação:\n') 
num2 = input('Digite o segundo número que deseja realizar uma operação: \n')
operador = input('Digite o operador (+, -, *, /):\n')

print(calculadora(num1, num2, operador))
