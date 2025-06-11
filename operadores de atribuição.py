saldo = 1000
saque = 500

saldo -= saque  # Realiza um saque
print(saldo)  # Saldo após o saque: 500
saldo += saque  # Reverte o saque
print(saldo)  # Saldo após reverter o saque: 1000
saldo *= 2  # Dobra o saldo
print(saldo)  # Saldo após dobrar: 2000
saldo /= 2  # Divide o saldo por 2
print(saldo)  # Saldo após dividir por 2: 1000.0
saldo %= 300  # Calcula o resto da divisão do saldo por 300
print(saldo)  # Resto da divisão: 1000 % 300 = 100
saldo **= 2  # Eleva o saldo ao quadrado
print(saldo)  # Saldo ao quadrado: 10000.0
saldo //= 3  # Realiza a divisão inteira do saldo por 3
print(saldo)  # Divisão inteira: 333.0