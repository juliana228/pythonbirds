class Conta:
    def __init__(self,numero_da_conta,nome,saldo):
        self.numero_da_conta = numero_da_conta
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self):

    def deposito(self):

    def saque(self):

    def mostraPessoa(self):
        print(f'Nome: {self.nome}, idade: {self.idade} anos, peso: {self.peso}kg, altura: {self.altura}cm')

lay = Pessoa('Lay', 19, 54, 163)
lay.mostraPessoa()
lay.envelhecer()
lay.emagrecer(3)
lay.mostraPessoa()

