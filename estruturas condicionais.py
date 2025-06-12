MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Digite sua idade: "))
if idade >= MAIOR_IDADE:
    print("Você é maior de idade.")
if idade < MAIOR_IDADE:
    print("Você é menor de idade.")

if idade >= MAIOR_IDADE:
    print("Você é maior de idade, pode tirar carteira de motorista.")
elif idade == IDADE_ESPECIAL:
    print("Você é menor de idade, mas pode tirar carteira de motorista com autorização dos pais.")  
else:
    print("Você é menor de idade, não pode tirar carteira de motorista.")