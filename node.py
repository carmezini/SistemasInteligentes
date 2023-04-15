class Node:
    def __init__(self, state, parent, move, cost, heuristic):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        if (self.heuristic):
            return (self.cost + self.heuristic) < (other.cost + other.heuristic)
        else:
            return (self.cost) < (other.cost)
