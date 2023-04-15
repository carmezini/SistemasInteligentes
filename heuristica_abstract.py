from abc import ABC, abstractmethod
from queue import PriorityQueue
from node import Node


class HeuristicaAbstract(ABC):
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.tempo_inicial = 0

    def get_blank_pos(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    def get_moves(self, state):
        # posicao em branco
        i, j = self.get_blank_pos(state)
        moves = []
        # movimentos válidos
        if i > 0:
            # esquerda
            moves.append((-1, 0))
        if i < 2:
            # direita
            moves.append((1, 0))
        if j > 0:
            # baixo
            moves.append((0, -1))
        if j < 2:
            # cima
            moves.append((0, 1))
        return moves

    def apply_move(self, state, move):
        i, j = self.get_blank_pos(state)
        x, y = move
        new_state = [row[:] for row in state]
        new_state[i][j], new_state[i+x][j +
                                        y] = new_state[i+x][j+y], new_state[i][j]
        return new_state

    def solve_puzzle(self):
        start_node = Node(self.initial_state, None, None, 0,
                          self.get_heuristic(self.initial_state))
        # fronteira = nodos a serem visitados
        frontier = PriorityQueue()
        frontier.put(start_node)
        # explored = nodos visitados
        explored = []

        while not frontier.empty():
            node = frontier.get()
            # tabuleiro completo
            if node.state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
                result = {
                    'len_explored': len(explored),
                    'final_cost': node.cost
                }
                return result
            # tabuleiro incompleto
            # add nodo aos nodos visitados
            explored.append(node.state)
            for move in self.get_moves(node.state):
                child_state = self.apply_move(node.state, move)
                if child_state not in explored:
                    child_cost = node.cost + 1
                    child_heuristic = self.get_heuristic(child_state)
                    child_node = Node(child_state, node, move,
                                      child_cost, child_heuristic)
                    frontier.put(child_node)
        return None

    @abstractmethod
    def get_heuristic(self, state):
        pass
