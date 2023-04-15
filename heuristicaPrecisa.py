from heuristica_abstract import HeuristicaAbstract


class HeuristicaPrecisa(HeuristicaAbstract):
    def __init__(self, initial_state):
        super().__init__(initial_state)

    def get_heuristic(self, state):
        """
        Calcula a menor distancia de cada peca ate sua posição final.
        Retorna um inteiro indicando o valor da heurística.
        """
        dist = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:
                    x, y = divmod(state[i][j]-1, 3)
                    dist += abs(x-i) + abs(y-j)
        return dist
