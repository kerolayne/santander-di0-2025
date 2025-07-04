#tipos de dados

#int
num1 = 10
print(num1)
print(type(num1))  # <class 'int'>
    
#float
num2 = 10.5
print(num2)
print(type(num2))  # <class 'float'>

#bool
num3 = True
print(num3)
print(type(num3))  # <class 'bool'>

#str
str1 = "Hello, World!"
print(str1)
print(type(str1))  # <class 'str'>

#constantes
PI = 3.14
print(PI)
print(type(PI))  # <class 'float'>

#conversão de tipos
num4 = 5

print(str(num4))  # converte int para str
print(float(num4))  # converte int para float

#comcatenar

texto = f"idade: {num4}, nome: {str1}"
print(texto)  # idade: 5, nome: Hello, World!

#conversão de tipos por divisão
num5 = 10

print(num5 / 2)  # resultado é float: 5.0
print(num5 // 2)  # resultado é int: 5

#coversão de numero para string
num6 = 123
print(str(num6))  # converte int para str: '123'

#funcao entrada e saida 

nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")  # Olá, nome digitado pelo usuário!

idade = int(input("Digite sua idade: "))
print(f"Você tem {idade} anos.")  # Você tem idade digitada pelo usuário!

print(nome, idade, end="...\n")  # Exibe nome e idade digitados pelo usuário
print(nome, idade, sep=", ", end="...\n")