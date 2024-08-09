class CalculaCorrida():
    km = Null
    precoKm = Null
    passageiro = Null
    
    def __init__(self, km, precoKm):
        self.km = km
        self.precoKm = precoKm
        super().__init__(km, precoKm)
        
    def getValor(km, precoKm):
        preco = self.km * self.precoKm
        return preco

class CorridaUberMoto(CalculaCorrida):
    def __init__(self, km):
        self.km = km
    def getValor():
        return 0.9 * super.getValor()

class CorridaUberX(CalculaCorrida):
    def __init__(self, km):
        self.km = km
    def getValor():
        return super.getValor()

class CorridaUberBlack(CalculaCorrida):
    def __init__(self, km):
        self.km = km
    def getValor():
        return 1.1 * super.getValor()

class CorridaUberPool(CalculaCorrida):
    def __init__(self, km, passageiro):
        self.passageiro = passageiro
        super().__init__(km, precoKm)
    def getValor():
        return super.getValor()/passageiro