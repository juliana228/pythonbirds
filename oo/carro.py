"""Você deve criar uma classe carro que vai posssuir 2 atributos
compostos por outras 2 classes
1) Motor
2) Direção
O motor terá a resposabilidade de controlar a velocide
Ele oferece os seguintes atributos:
1) atributo de dado velocidade
2) método acelerar que deverá incrementar a velocidade de uma unidade
3) método frear que deverá decrementar a velocidade em 2 unidades

A direção terá a resposabilidade de controlar a direção. Ela oferece os seguites atributos:
1) valor de direção com valores possíveis (norte, sul, leste, oeste)
2) método girar_a_ireita
3) método girar_a_esquerda

   N
O     L
   S

       Exemplo:
       >>> #Testando motor
       >>> motor = Motor()
       >>> motor.velocidade
       0
       >>> motor.acelerar()
       >>> motor.velocidade
       1
       >>> motor.acelerar()
       >>> motor.velocidade
       2
       >>> motor.acelerar()
       >>> motor.velocidade
       3
       >>> motor.frear()
       >>> motor.velocidade
       1
       >>> motor.acelerar()
       >>> motor.velocidade
       0

       >>> #Testando Direção
       >>> direcao = Direcao()
       >>> direcao.valor
       'Norte'
       >>> direcao.girar_a_direita()
       >>> direcao.valor
       'Leste'
       >>> direcao.girar_a_direita()
       >>> direcao.valor
       'Sul'
       >>> direcao.girar_a_direita()
       >>> direcao.valor
       'Oeste'
       >>> direcao.girar_a_direita()
       >>> direcao.valor
       'Norte'
       >>> direcao.girar_a_esquerda()
       >>> direcao.valor
       'Oeste'
       >>> direcao.girar_a_esquerda()
       >>> direcao.valor
       'Sul'
       >>> direcao.girar_a_esquerda()
       >>> direcao.valor
       'Leste'
       >>> direcao.girar_a_esquerda()
       >>> direcao.valor
       'Norte'
       >>> carro = Carro(direcao,motor)
       >>> carro.calcular_velocidade()
       0
       >>> carro.acelerar()
       >>> carro.calcular_velocidade()
       1
       >>> carro.acelerar()
       >>> carro.calcular_velocidade()
       2
       >>> carro.frear()
       >>> carro.calcular_velocidade()
       0
       >>> carro.calcular_direcao()
       >>> 'Norte'
       >>> carro.girar_a_direita()
       >>> carro.calcular_direcao()
       >>> 'Leste'
       >>> carro.girar_a_esquerda()
       >>> carro.calcular_direcao()
       >>> 'Norte'
       >>> carro.girar_a_esquerda()
       >>> carro.calcular_direcao()
       >>> 'Oeste'
"""
class Carro():
    def __init__(self,motor,direcao):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade
    def calcular_direcao(self):
        return self.direcao.valor
    def acelerar(self):
        return self.motor.acelerar()
    def frear(self):
        return  self.motor.frear()
    def girar_a_direita(self):
        return self.direcao.girar_a_direita()
    def girar_a_esquerda(self):
        return  self.direcao.girar_a_esquerda()

class Motor():
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1
    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0,self.velocidade)

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'
class Direcao():

    rotacao_a_direita_dct = {NORTE:LESTE,LESTE:SUL,SUL:OESTE,OESTE:NORTE}
    rotacao_a_esquerda_dct = {NORTE:OESTE,OESTE:SUL,SUL:LESTE,LESTE:NORTE}
    def __init__(self):
        self.valor = NORTE
    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]
    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]
carro = Carro()

