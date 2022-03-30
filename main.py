import os
import datetime
import timeit
# implementar interface gráfica
# implementar alias para Jogador 1 e Jogador 2

print(f'\nJogo da velha \nX|X|X\t0|0|0\nX|X|X\t0|0|0\nX|X|X\t0|0|0\n')

tabuleiro = [['00','01','02'],[11,12,13],[20,21,22]]
jogo = [[]]

'''for linha in tabuleiro:
    for coluna in tabuleiro:
        print(coluna)
'''

# se as linhas ou colunas forem iguais = ponto
# se a linha e coluna for incrementando +1 ou -1 = ponto

# se 0 1 2 , 3 4 5 , 6 7 8 = vitoria horizontal
# se 0 3 6, 1 4 7, 2 5 8 = vitoria vertical
# se 0 4 8 , 2 4 6 = vitória diagonal

def ValidaPonto():
    if jogo[0][0] == jogo[0][1] == jogo[0][2] or jogo[1][0] == jogo[1][1] == jogo[1][2] or jogo[1][0] == jogo[1][1] == jogo[1][2]:
        # ponto
    elif jogo[0][0] == jogo[1][0] == jogo[2][0] or jogo[0][1] == jogo[1][1] == jogo[2][1] or jogo[0][2] == jogo[1][2] == jogo[2][2]:
        #ponto
    elif jogo[0][0] == jogo[1][1] == jogo[2][2] or jogo[0][3] == jogo[1][1] == jogo[2][1]:
        #ponto
    else
        #nenhum ponto
        return...