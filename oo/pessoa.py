class Pessoa:
    def __init__(self,nome='Bey',idade=40):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        print(f'Olá {p.nome}')

p = Pessoa()
p.cumprimentar()
print(p.nome)
print(p.idade)
p.nome = 'Rih'
print(p.nome)





