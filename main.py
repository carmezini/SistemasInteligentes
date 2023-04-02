from tabuleiro import Tabuleiro
from heuristicaSimples import HeuristicaSimples
from menu import Menu



def iniciar():
  opcoes = {
    1:'Custo Uniforme',
    2:'Heurística simples',
    3:'Heurística mais precisa'
  }
  
  menu = Menu('Busca heurística', opcoes)
  op =  menu.pergunte()
  inicio = Tabuleiro(input('Insira o tabuleiro inicial:'))

  heuristicas = {
    1:'Custo Uniforme',
    2: HeuristicaSimples(inicio).calcularHeuristica(),
    3:'Heurística mais precisa'
  }
  
  heuristicas[op]

iniciar()