class Pessoa:
    olhos = 2
    def __init__(self,nome=None,idade=40,*filhos):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

p = Pessoa()
blue = Pessoa(nome='blue')
beyonce = Pessoa(blue,idade=40)
print(Pessoa.olhos)
print(blue.olhos)
print(beyonce.olhos)







