# Definindo a classe bicicleta com atributos e métodos
class bicicleta:
    def __init__(self,cor, modelo, ano, preco):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
    
    def buzinar(self):
        print("Buzina da bicicleta!")

    def parar(self):
        print("Parando a bicicleta!")
    
    def pedalar(self):
        print("Pedalando a bicicleta!")

bicicleta1 = bicicleta("azul", "mountain", 2020, 1500.00)

bicicleta1.buzinar()
bicicleta1.parar()  
bicicleta1.pedalar()

print(f"Cor: {bicicleta1.cor}")
print(f"Modelo: {bicicleta1.modelo}")
print(f"Ano: {bicicleta1.ano}")
print(f"Preço: {bicicleta1.preco}")
