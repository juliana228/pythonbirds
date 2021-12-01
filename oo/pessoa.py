class Carro:
    def __init__(self, marca, preco, cor):
        self.marca = marca
        self.cor = cor
        self.preco = preco

    def ligar(self):
        print('Ligando o carro')

    def desligar(self):
        print('desligando o carro')

    def ExibirInformacoes(self):
        print(f'O carro é da marca {self.marca}, custa R$ {self.preco} e possui cor {self.cor}')

carro1 = Carro('Honda',150000,'vermelha')
carro1.ligar()
carro1.desligar()
carro1.ExibirInformacoes()
