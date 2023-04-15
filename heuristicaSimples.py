from heuristica_abstract import HeuristicaAbstract


class HeuristicaSimples(HeuristicaAbstract):
    def __init__(self, initial_state):
        super().__init__(initial_state)

    def get_heuristic(self, state):
        """
        Calcula a quantidade de peças fora de sua posição final.
        Retorna um inteiro indicando o valor da heurística.
        """
        # estado objetivo (peças na posição final)
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        # contador de peças fora de posição
        misplaced = 0

        for i in range(3):
            for j in range(3):
                if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                    misplaced += 1
        return misplaced
