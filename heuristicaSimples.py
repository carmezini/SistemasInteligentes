class HeuristicaSimples:
    def __init__(self, inicio) -> None:
        self.objetivo = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.nodosAbertos = [inicio]
        self.nodosVisitados = []

    def calcularHeuristica(self):
        for nodo in self.nodosAbertos:
            tabuleiro = nodo.getTabuleiro()
            score = 0
            
            for linha in range (3):
                for col in range (3):
                    if(self.foraDoLugar(tabuleiro[linha][col], linha, col)):
                        score += 1
                        nodo.score = score
        if score == 0:
            self.jogoTerminou()

    def criarNodos(self):
       menor = self.nodosAbertos[0]
       for nodo in self.nodosAbertos:
            if nodo.score <= menor.score:
                menor = nodo

    def foraDoLugar(self, peca, x, y):
        if peca != '0':
            posicao = True
            for linha in range (len(self.objetivo)):
                try:
                    if self.objetivo[linha].index(int(peca)) == y and linha == x:
                        posicao = False
                        break
                except ValueError:
                    pass
            return posicao
        else:
            return False

    def jogoTerminou(self, nodo):
        estadoAtual = nodo