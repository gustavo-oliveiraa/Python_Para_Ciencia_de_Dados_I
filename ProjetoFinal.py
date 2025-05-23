# -*- coding: utf-8 -*-
"""
Created on Wed May 21 17:00:42 2025

@author: PC
"""

# Trabalho Final

import time
import os

def Limpar_Tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def Exibir_Menu():
    print("-" * 70)
    print(' ' * 10, 'Olá! Bem-vindo ao nosso Sistema de Estoque')
    print("-" * 70)
    print('Menu de Opções:')
    print('1 - Adicionar Produtos ao Estoque')
    print('2 - Remover Produtos do Estoque')
    print('3 - Buscar Informações de um Produto')
    print('4 - Remover um Produto Completamente')
    print('5 - Imprimir o Estoque Atual')
    print('6 - Calcular o Valor Total do Estoque')
    print('0 - Sair do menu de opções')
    print("-" * 70)
    
def solicitar_numero(mensagem, tipo=int):
    while True:
        try:
            return tipo(input(mensagem))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
    
def AdicionarProdutosEstoque(estoque):
    produto = input('Digite o nome do produto que deseja criar ou adicionar unidades: ').strip().lower()
        
    if produto in estoque:
        quantidade = solicitar_numero(f'Digite a nova quantidade para adicionar ao produto "{produto.capitalize()}": ')
        estoque[produto]['quantidade'] += quantidade
        print(f"\n{produto.capitalize()} atualizado. Nova quantidade: {estoque[produto]['quantidade']}. Valor: R$ {estoque[produto]['valor']:.2f}")        
    else:
        quantidade = solicitar_numero(f'Digite a quantidade inicial do produto "{produto.capitalize()}": ')
        valor = solicitar_numero(f'Digite o valor unitário de "{produto.capitalize()}": R$ ', float)
        estoque[produto] = {
            'quantidade': quantidade,
            'valor': valor
        }
        print(f"\n{produto.capitalize()} criado com sucesso. Quantidade: {quantidade}. Valor: R$ {valor:.2f}")
    
    time.sleep(5)
        
    
def RemoverProdutosEstoque(estoque):
    produto = input('Digite o nome do produto que deseja remover unidades: ').strip().lower()
    
    if produto in estoque:
        quantidade = solicitar_numero(f'Quantas unidades deseja remover do produto "{produto.capitalize()}": ')
        
        if quantidade >= estoque[produto]['quantidade']:
            print(f'A quantidade informada é maior ou igual a que temos no estoque. Removendo tudo.')
            estoque[produto]['quantidade'] = 0
        else:
            estoque[produto]['quantidade'] -= quantidade
            
        print(f"\n{produto.capitalize()} atualizado. Nova quantidade: {estoque[produto]['quantidade']}. Valor: R$ {estoque[produto]['valor']:.2f}")

    else:
        print('\nProduto não encontrado no estoque!')
        
    time.sleep(5)
        

def BuscarInformacoesProduto(estoque):
    produto = input('Digite o nome do produto que deseja obter informações: ').strip().lower()
    if produto in estoque:
        print("\nProduto".ljust(20), "Quantidade".ljust(12), "Valor".ljust(10))
        print("-" * 45)
        print(produto.capitalize().ljust(20), str(estoque[produto]['quantidade']).ljust(12), f"R$ {estoque[produto]['valor']:.2f}".ljust(10))
    else:
        print(f"\n{produto.capitalize()} não encontrado. Quantidade: 0. Valor: R$ 0.00")
        
    time.sleep(5)
        
def RemoverProdutoCompletamente(estoque):
    produto = input("Digite o nome do produto que deseja remover do nosso estoque: ").strip().lower()
    if produto in estoque:
        opc = input(f'Tem certeza que deseja remover "{produto.capitalize()}" completamente? (S/N): ').strip().upper()
        if opc == 'S':
            del estoque[produto]
            print(f"\n{produto.capitalize()} removido com sucesso!")
        elif opc == 'N':
            print('\nOperação cancelada. Retornando ao menu...')            
        else:
            print('\nOpção inválida!')
    else:
        print('\nProduto não encontrado no estoque!')
        
    time.sleep(5)
    
    
def ImprimirEstoqueAtual(estoque):
    #if len(estoque) == 0:
    if not estoque:
        print('\nO estoque no momento se encontra vazio...')
    else:
        print("\nProduto".ljust(20), "Quantidade".ljust(12), "Valor".ljust(10))
        print("-" * 45)
        for produto in sorted(estoque):
            print(produto.capitalize().ljust(20), str(estoque[produto]['quantidade']).ljust(12), f"R$ {estoque[produto]['valor']:.2f}".ljust(10))
            #print(f"{produto} | Quantidade: {estoque[produto]['quantidade']} | Valor: R$ {estoque[produto]['valor']:.2f}")
    
    time.sleep(5)
    
def CalcularValorTotalEstoque(estoque):
    total = 0
    for produto in estoque:
        valor = estoque[produto]['quantidade'] * estoque[produto]['valor']
        total += valor
    print(f'\nO valor total do estoque é R$ {total:.2f}')
    
    time.sleep(5)
    
def EncerrarPrograma():
    print("-" * 70)
    print(" " * 15 + "Sistema encerrado. Até logo!")
    print("-" * 70)
    
    time.sleep(5)
        
estoque = {}
opcao = -1

while opcao != 0:
    Limpar_Tela()
    Exibir_Menu()
    try:
        opcao = int(input("Qual opção deseja: "))
    except ValueError:
        print('Erro: você deve digitar um número.')
        time.sleep(3)
        continue
    
    Limpar_Tela()
    
    if opcao == 1:
        AdicionarProdutosEstoque(estoque)
    elif opcao == 2:
        RemoverProdutosEstoque(estoque)
    elif opcao == 3:
        BuscarInformacoesProduto(estoque)
    elif opcao == 4:
        RemoverProdutoCompletamente(estoque)
    elif opcao == 5:
        ImprimirEstoqueAtual(estoque)
    elif opcao == 6:
        CalcularValorTotalEstoque(estoque)
    elif opcao == 0:
        confirmacao = input('Tem certeza que deseja sair? (S/N): ').strip().upper()
        if confirmacao == 'S':            
            EncerrarPrograma()
            break
        else:
            print("Retornando ao menu...")
            opcao = -1
            time.sleep(3)
    else:
        print('Opção inválida. Tente novamente.')
        time.sleep(5)
