saldo = 1000
saque = 500
limite = 2000
conta_especial = True

# Operadores lógicos
print(True and True)  # True
print(True and False)  # False
print(False and False)  # False
print(False or True)  # True
print(True or True)  # True
print(False or False)  # False

expressao1 = saldo >= saque and saldo <= limite or conta_especial and saldo >= saque
print(expressao1)  # Verifica se o saldo é suficiente para o saque considerando o limite e conta especial
expressao2 = saldo >= saque and saldo <= limite or conta_especial and saldo >= saque
print(expressao2)  # Verifica se o saldo é suficiente para o saque considerando o limite e conta especial


# Operadores de identidade
print("Operadores de identidade")
print(saldo is saque)  # Verifica se saldo e saque são o mesmo objeto (False)
print(saldo is not saque)  # Verifica se saldo e saque não são o mesmo objeto (True)  

# Operadores de associação
print("Operadores de associação")
lista = [1, 2, 3, 4, 5]
print(1 in lista)  # Verifica se 1 está na lista (True)
print(6 in lista)  # Verifica se 6 está na lista (False)
print(1 not in lista)  # Verifica se 1 não está na lista (False)
print(6 not in lista)  # Verifica se 6 não está na lista (True)