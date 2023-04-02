from tabuleiro import Tabuleiro

class Nodo:
  def __init__(self, id, estado) -> None:
      self.id = id
      self.path = []
      self.score = 0
      self.tabuleiro = Tabuleiro(estado)

  def getTabuleiro(self):
    return self.tabuleiro