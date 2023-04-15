from custoUniforme import CustoUniforme
from heuristicaSimples import HeuristicaSimples
from heuristicaPrecisa import HeuristicaPrecisa
import time


class Menu:
    def __init__(self):
        self.title = 'Busca heurística'
        self.options = {
            1: 'Custo Uniforme',
            2: 'Heurística simples',
            3: 'Heurística mais precisa',
            4: "Todas heuristicas",
            5: "Sair"
        }

    def ask(self):
        self.show()
        return self.read_option()

    def show(self):
        msg_title = '==== {}'.format(self.title)
        print(msg_title)
        for (k, v) in self.options.items():
            print('[{}] {}'.format(k, v))
        print('====')

    def read_option(self):
        op = self.read_int()
        while op not in self.options:
            print('Opção inválida!')
            op = self.read_int()
        return op

    def read_int(self):
        read = False
        while not read:
            try:
                number = int(input('Digite sua opção : '))
                read = True
            except ValueError:
                print('Erro! Digite um número int maior ou igual a zero.')
        return number

    def initial_state(self):
        initial_state = (input('Insira o tabuleiro inicial:')).split()
        initial_state = [int(x) for x in initial_state]
        initial_state = [(initial_state[i:i + 3])
                         for i in range(0, len(initial_state), 3)]
        return initial_state

    def show_results(self, option, result, tempo_total):
        print("\n---- " + option)
        print(f'Total caminho: {result["final_cost"]}')
        print(f'Total nodos visitados: {result["len_explored"]}')
        print(f'Movimentos: {result["moves"]}')
        print(f"{(tempo_total):.4f} segundos\n")

    def start(self):
        while (True):
            op = self.ask()

            if (op == 5):
                exit()

            initial_state = self.initial_state()
            heuristics = {
                1: CustoUniforme(initial_state),
                2: HeuristicaSimples(initial_state),
                3: HeuristicaPrecisa(initial_state)
            }

            if (op == 4):
                for op, h in heuristics.items():
                    init_time = time.time()  # em segundos
                    result = h.solve_puzzle()
                    final_time = time.time()  # em segundos
                    self.show_results(self.options[op],
                                      result, final_time - init_time)
            else:
                init_time = time.time()  # em segundos
                result = heuristics[op].solve_puzzle()
                final_time = time.time()  # em segundos
                self.show_results(self.options[op],
                                  result, final_time - init_time)
