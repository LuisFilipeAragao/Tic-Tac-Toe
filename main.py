import os
import datetime
import timeit
# implementar interface gráfica
# implementar alias para Jogador 1 e Jogador 2

print(f'\nTIC\nX|X|X\t0|0|0\nX|X|XTAC0|0|0\nX|X|X\t0|0|0\n\t\t  TOE')

tabuleiro = [['','',''],['','',''],['','','']]
jogador1 = ""
jogador2 = ""
lance = 0

'''for linha in tabuleiro:
    for coluna in tabuleiro:
        print(coluna)

'''
'''print(f'Escolha o seu nome, Jogador 1: ')
jogador1 = input()

print(f'Escolha o seu nome, Jogador 2: ')
jogador2 = input()

print(f'Preparados? {jogador1} e {jogador2}.\nComeçar!!!')'''

while lance in range(10):
    print(f'Escolha um número no tabuleiro:\n1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9')

    lance +=1

# se as linhas ou colunas forem iguais = ponto
# se a linha e coluna for incrementando +1 ou -1 = ponto

# se 0 1 2 , 3 4 5 , 6 7 8 = vitoria horizontal
# se 0 3 6, 1 4 7, 2 5 8 = vitoria vertical
# se 0 4 8 , 2 4 6 = vitória diagonal

