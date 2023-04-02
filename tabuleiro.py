class Tabuleiro:
  def __init__(self, estado) -> None:
    if estado:
      n = 3
      estado = estado.split()
      self.ehValido(estado)
      self.tabuleiro = [estado[i:i + n] for i in range(0, len(estado), n)]
    else:
      self.tabuleiro = [[6, 7, 5], [1, 2, 3], [0, 4, 8]]

  def getTabuleiro(self):
    return self.tabuleiro
  
  def ehValido(self, estado):
    try:
      if(len(estado) == 9):
        pass
      else:
        raise IndexError
      for i in estado:
        if int(i):
          pass
    except IndexError:
      print('Array deve ter 9 posicoes')
    except ValueError:
      print('Deve conter apenas numeros')
    

