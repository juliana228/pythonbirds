class bombaCombustivel:
    def __init__(self, tipoCombustivel,valorLitro=5,quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
    def abastecerPorValor(self,valor):
        qtd_litros = valor/valorLitro
bomba = bombaCombustivel('gasolina',5,)