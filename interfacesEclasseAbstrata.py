class Pessoas:
    def __init__(self, nome = None, idade = None):
        self.nome = nome
        self.idade = idade
    @classmethod
    def criar_a_partir_data_nascimento(cls, ano, mes, dia, nome):
        from datetime import datetime
        data_nascimento = datetime(ano, mes, dia)
        idade = (datetime.now() - data_nascimento).days // 365
        return cls(nome, idade)


p = Pessoas("João", 30)
print(p)

p2 = Pessoas.criar_a_partir_data_nascimento(ano = 1990, mes = 5, dia = 15, nome = "Maria")
print(p2.nome, p2.idade)