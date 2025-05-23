# -*- coding: utf-8 -*-
"""
Created on Fri May 23 15:49:42 2025

@author: PC
"""

frutas = []

while True:
    fruta = input("Digite o nome de uma fruta (ou 'sair' para encerrar): ").strip().lower()
    if fruta == "sair":
        break
    frutas.append(fruta)

dicionario_frutas = {fruta: len(fruta) for fruta in frutas}

frutas_maiores_que_5 = [fruta for fruta in frutas if len(fruta) > 5]

frutas_ordenadas = sorted(frutas_maiores_que_5)

print("\nFrutas com mais de 5 letras (ordenadas):")
for fruta in frutas_ordenadas:
    print(fruta)
