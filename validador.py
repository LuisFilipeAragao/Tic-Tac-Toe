def ValidaPonto(self, jogada):
    jogada = self.jogada
    if jogada[0][0] == jogada[0][1] == jogada[0][2] or jogada[1][0] == jogada[1][1] == jogada[1][2] or jogada[1][0] == jogada[1][1] == jogada[1][2]:
        ...
    elif jogada[0][0] == jogada[1][0] == jogada[2][0] or jogada[0][1] == jogada[1][1] == jogada[2][1] or jogada[0][2] == jogada[1][2] == jogada[2][2]:
        ...
    elif jogada[0][0] == jogada[1][1] == jogada[2][2] or jogada[0][3] == jogada[1][1] == jogada[2][1]:
        ...
    else:
        #nenhum ponto
        return...