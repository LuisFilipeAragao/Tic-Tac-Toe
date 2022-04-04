import os
import datetime
import timeit
from termcolor import colored
# implementar interface gráfica
# implementar alias para Jogador 1 e Jogador 2

def AtulizaJogo():
    print(f'{tabuleiro["1"]}|{tabuleiro["2"]}|{tabuleiro["3"]}\n{tabuleiro["4"]}|{tabuleiro["5"]}|{tabuleiro["6"]}\n{tabuleiro["7"]}|{tabuleiro["8"]}|{tabuleiro["9"]}')

def ValidaPonto():
    if tabuleiro['1'] == tabuleiro['2'] == tabuleiro['3'] or tabuleiro['4'] == tabuleiro['5'] == tabuleiro['6'] or tabuleiro['7'] == tabuleiro['8'] == tabuleiro['9'] and not "":
        print("Vitória horizontal do jogador tal")
    elif tabuleiro['1'] == tabuleiro['4'] == tabuleiro['7'] or tabuleiro['2'] == tabuleiro['5'] == tabuleiro['8'] or tabuleiro['3'] == tabuleiro['6'] == tabuleiro['9'] and not "":
        print("Vitória vertical do jogador tal")
    elif tabuleiro['1'] == tabuleiro['5'] == tabuleiro['9'] or tabuleiro['3'] == tabuleiro['5'] == tabuleiro['7'] and not "":
        print("Vitória diagonal do jogador tal")
    else:
        ...

def jogada(jogo):
    lance = jogo
    print(f">>Jogada {lance}!!!")
    if lance %2 == 0:lui
        posicao1 = 0
        print(f'Escolha a posição (1-9), {jogador1}: ')
        posicao1 = input()
        if tabuleiro[f"{posicao1}"] == "":
            tabuleiro[f"{posicao1}"] = "X"
            #ValidaPonto()
            AtulizaJogo()
        else:
            print(f'A posição {colored(posicao1,"red")} já foi preenchida, informar uma nova: ')
            AtulizaJogo()
            jogada(lance)
    else:
        posicao2 = 0
        print(f'Escolha a posição (1-9), {jogador2}: ')
        posicao2 = input()
        if tabuleiro[f"{posicao2}"] == "":
            tabuleiro[f"{posicao2}"] = "0"
            #ValidaPonto()
            AtulizaJogo()
        else:
            print(f'A posição {colored(posicao2,"red")} já foi preenchida, informar uma nova: ')
            AtulizaJogo()
            jogada(lance)

def jogo():

    print(f'Escolha o seu nome, Jogador 1 (X): ')
    jogador1 = input()

    print(f'Escolha o seu nome, Jogador 2 (O): ')
    jogador2 = input()

    print(f'Preparados? {jogador1} e {jogador2}.\nComeçar!!!')

    print(f'Escolha um número no tabuleiro:\n1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9')

    for lance in range(9):
        jogada(lance)


print(f'\nTIC\nX|X|X\t0|0|0\nX|X|XTAC0|0|0\nX|X|X\t0|0|0\n\t\t  TOE')
jogador1 = ""
jogador2 = ""
jogador1jogo = []
jogador2jogo = []
lance = 0
tabuleiro = {"1":"", "2":"", "3":"", "4":"", "5":"", "6":"", "7":"", "8":"", "9":"" }

jogo()

print("Fim do jogo, jogar novamente?(s/n)")

if input() == "s":
    for i in list(range(1,10)):
        tabuleiro[f'{i}'] = ""
    jogo()
else:
    print("Obrigado por jogar!")

#corrigir a alternância entre jogadas/preenchimento jogador 2
#corrigir um breakpoint quando houver vitória