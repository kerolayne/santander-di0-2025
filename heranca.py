class veiculo:
    def __init__(self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa

    def info(self):
        return f"Veículo: {self.marca} {self.modelo} - Placa: {self.placa}"
    
class carro(veiculo):
    def __init__(self, marca, modelo, placa, portas):
        super().__init__(marca, modelo, placa)
        self.portas = portas

    def info(self):
        return f"{super().info()} - Portas: {self.portas}"
    
class moto(veiculo):
    def __init__(self, marca, modelo, placa, cilindrada):
        super().__init__(marca, modelo, placa)
        self.cilindrada = cilindrada

    def info(self):
        return f"{super().info()} - Cilindrada: {self.cilindrada}cc"
    
class caminhão(veiculo):
    def __init__(self, marca, modelo, placa):
        super().__init__(marca, modelo, placa)

    def info(self):
        return f"{super().info()} - Caminhão"
    
# Exemplo de uso
carro1 = carro("Toyota", "Corolla", "ABC-1234", 4)
moto1 = moto("Honda", "CB500", "XYZ-5678", 500)
caminhao = caminhão("Volvo", "FH", "LMN-9101")

print(carro1.info())
print(moto1.info()) 
print(caminhao.info()) 

#herança multipla
# Definindo a classe animal com um método genérico

class animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas


class mamifero(animal):
    def __init__(self, cor_pelo, **kwargs):
        self.cor_pelo = cor_pelo
        super().__init__(**kwargs)

class ave(animal):
    def __init__(self, cor_bico, **kwargs):
        self.cor_bico = cor_bico
        super().__init__(**kwargs)


class gato(mamifero):
    pass

class ornintorinco(ave, mamifero):
    pass

gato1 = gato(nro_patas = 2, cor_pelo = "Cinza")
ornitorrinco1 = ornintorinco(nro_patas = 4, cor_pelo = "Marrom", cor_bico = "Preto")
print(f"Gato: {gato1.nro_patas} patas, cor do pelo: {gato1.cor_pelo}")
print(f"Ornitorrinco: {ornitorrinco1.nro_patas} patas, cor do pelo: {ornitorrinco1.cor_pelo}, cor do bico: {ornitorrinco1.cor_bico}")