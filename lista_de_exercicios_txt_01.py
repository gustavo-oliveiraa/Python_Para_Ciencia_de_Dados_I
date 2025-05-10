# -*- coding: utf-8 -*-
"""
Created on Wed May  7 12:04:07 2025

@author: PC
"""

# Lista de exercícios txt

"""
1.  Crie uma função que analise o tipo de dado do argumento. Caso a entrada seja Int, quero que retorne float, e caso a entrada seja float, quero que retorne Int.
Se entrar outro tipo, printar "Tipo não suportado".
"""

def analise_tipo_dado (dado):
    if type(dado) == type(1):
        return float(dado)
    elif type(dado) == type(1.0):
        return int(dado)
    else:
        return 'Tipo não suportado'
    
#print(analise_tipo_dado('ssa'))

entrada = input("Digite um dado:\n")

try: 
    valor = int(entrada)
except ValueError:
    try:
        valor = float(entrada)
    except ValueError:
        valor = entrada
        
print(analise_tipo_dado(valor))
