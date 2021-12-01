class Filme:
    def __init__(self,nome):
        self.nome = nome
    def MudarNome(self):
        perg = input(f'Quer trocar o filme ?')
        if perg == 's':
            novo_nome = input('Qual o filme ?')
            self.nome = novo_nome
        else:
            print(f'O filme que você vai ver ainda é {self.nome}')
    def MostrarNome(self):
        print(f'Filme: {self.nome}')

def main():
    filme = Filme('titanic')
    while True:
        filme.MostrarNome()
        filme.MudarNome()

    filme.MostrarNome()
main()








