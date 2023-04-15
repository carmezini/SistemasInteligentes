from heuristica_abstract import HeuristicaAbstract


class CustoUniforme(HeuristicaAbstract):
    def __init__(self, initial_state):
        self.initial_state = initial_state

    def get_heuristic(self, state):
        return None
