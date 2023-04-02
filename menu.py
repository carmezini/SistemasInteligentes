class Menu:
    def __init__(self, titulo, opcoes):
        self.titulo = titulo
        self.opcoes = opcoes

    def pergunte(self):
        self.mostre()
        return self.leia_opcao()

    def mostre(self):
        msg_titulo = '==== {}'.format(self.titulo)
        print(msg_titulo)
        for (k,v) in self.opcoes.items():
            print('[{}] {}'.format(k,v))
        print('====')

    def leia_opcao(self):
        op = self.leia_inteiro('Digite sua opção : ')
        while op not in self.opcoes:
            print('Opção inválida!')
            op = self.leia_inteiro('Digite sua opção : ')
        return op

    def leia_inteiro(self, msg):
        leu = False
        while not leu:
            try:
                numero = int(input(msg))
                leu = True
            except ValueError:
                print('Erro! Digite um número inteiro maior ou igual a zero.')
        return numero
