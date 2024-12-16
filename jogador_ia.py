# -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro : Tabuleiro, tipo : int):
        super().__init__(tabuleiro, tipo)

    def check_line(self, line):
        if line.count(Tabuleiro.JOGADOR_0) == 2 and line.count(Tabuleiro.DESCONHECIDO) == 1:
            return line.index(Tabuleiro.DESCONHECIDO)
        elif line.count(Tabuleiro.JOGADOR_X) == 2 and line.count(Tabuleiro.DESCONHECIDO) == 1:
            return line.index(Tabuleiro.DESCONHECIDO)
        return None
    
    def check_R1(self):
        """Se você ou seu oponente tiver duas marcações em sequência, marque o quadrado restante"""

        #Checando linhas 
        for i in range(3):
            j = self.check_line([self.matriz[i][0], self.matriz[i][1], self.matriz[i][2]])
            if j is not None:
                print(f"Encontrei na linha {i} {j}")
                return (i, j)
        
        #Checando colunas
        for i in range(3):
            j = self.check_line([self.matriz[0][i], self.matriz[1][i], self.matriz[2][i]])
            if j is not None:
                print(f"Encontrei na coluna {j} {i}")
                return (j, i)

        #Checando diagonal principal
        diag_p = self.check_line([self.matriz[i][i] for i in range(3)])
        if diag_p is not None:
            print(f"Encontrei na diagonal1 {diag_p} {diag_p}")
            return (diag_p, diag_p)
        
        #Checando diagonal secundária
        diag_s = self.check_line([self.matriz[i][2-i] for i in range(3)])
        if diag_s is not None:
            print(f"Encontrei na diagonal2 {diag_s} {diag_s}")
            return (diag_s, 2-diag_s)
        
        return None
    
    def check_R2(self):
        """Se houver uma jogada que crie duas sequências de duas marcações, use-a."""
        if self.matriz[1][0] == self.matriz[0][1] != Tabuleiro.DESCONHECIDO and self.matriz[0][0] == Tabuleiro.DESCONHECIDO:
            return (0, 0)
        elif self.matriz[0][1] == self.matriz[1][2] != Tabuleiro.DESCONHECIDO and self.matriz[0][2] == Tabuleiro.DESCONHECIDO:
            return (0, 2)
        elif self.matriz[1][2] == self.matriz[2][1] != Tabuleiro.DESCONHECIDO and self.matriz[2][2] == Tabuleiro.DESCONHECIDO:
            return (2, 2)
        elif self.matriz[2][1] == self.matriz[1][0] != Tabuleiro.DESCONHECIDO and self.matriz[2][0] == Tabuleiro.DESCONHECIDO:
            return (2, 0)
        return None
    
    def check_R3(self):
        """Se o quadrado central estiver livre, marque-o."""
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)
        return None

    def check_R4(self):
        """Se seu oponente tiver marcado um dos cantos, marque o canto oposto."""
        if self.matriz[0][0] == Tabuleiro.JOGADOR_X and self.matriz[2][2] == Tabuleiro.DESCONHECIDO:
            return (2, 2)
        elif self.matriz[0][2] == Tabuleiro.JOGADOR_X and self.matriz[2][0] == Tabuleiro.DESCONHECIDO:
            return (2, 0)
        elif self.matriz[2][0] == Tabuleiro.JOGADOR_X and self.matriz[0][2] == Tabuleiro.DESCONHECIDO:
            return (0, 2)
        elif self.matriz[2][2] == Tabuleiro.JOGADOR_X and self.matriz[0][0] == Tabuleiro.DESCONHECIDO:
            return (0, 0)
        return None
    
    def check_R5(self):
        """Se houver um canto vazio, marque-o."""
        if self.matriz[0][0] == Tabuleiro.DESCONHECIDO:
            return (0, 0)
        elif self.matriz[0][2] == Tabuleiro.DESCONHECIDO:
            return (0, 2)
        elif self.matriz[2][0] == Tabuleiro.DESCONHECIDO:
            return (2, 0)
        elif self.matriz[2][2] == Tabuleiro.DESCONHECIDO:
            return (2, 2)
        return None

    def getJogada(self) -> (int, int):
        feitas = []
        restantes = []
        
        # Criando lista com jogadas possíveis
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    restantes.append((l, c))
                else:
                    feitas.append((l, c))

        # Checando jogada
        R1 = self.check_R1()
        if R1 is not None:
            return R1
        
        R2 = self.check_R2()
        if R2 is not None:
            return R2
        
        R3 = self.check_R3()
        if R3 is not None:
            return R3
        
        R4 = self.check_R4()
        if R4 is not None:
            return R4
        
        R5 = self.check_R5()
        if R5 is not None:
            return R5

        # R6: Marque arbitrariamente um quadrado vazio.
        if(len(restantes) > 0):
            p = randint(0, len(restantes)-1)
            return restantes[p]
        else:
           return None