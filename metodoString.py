nome = "kerolayne"

print(nome.upper())  # Converte para maiúsculas: KEROLAYNE
print(nome.lower())  # Converte para minúsculas: kerolayne
print(nome.title())  # Converte para título: Kerolayne

texto = "   Olá, mundo!   "
print(texto + ".")  # Imprime o texto original com espaços: "   Olá, mundo!   "
print(texto.strip() + ".")  # Remove espaços em branco no início e no final: "Olá, mundo!"
print(texto.lstrip() + ".")  # Remove espaços em branco no início: "Olá, mundo!   "
print(texto.rstrip() + ".")  # Remove espaços em branco no final: "   Olá, mundo!"

menu = "python" 

print("####" + menu + "####")  # Concatena "####" com a string "python": ####python####)
print(menu.center(20, "#"))  # Centraliza a string "python" em um campo de 20 caracteres, preenchendo com "#": #######python#######
print("-".join(menu))  # Junta os caracteres da string "python" com "-" entre eles: p-y-t-h-o-n

#=---------------------------------------------

#formatação de strings
profissao = "Programadora"
linguagem = "Python e JavaScript"
print(f"Eu sou {profissao} e estou aprendendo {linguagem}.")  # Formatação com f-strings
print("Eu sou {} e estou aprendendo {}.".format(profissao, linguagem))  # Formatação com .format()
print("Eu sou %s e estou aprendendo %s." % (profissao, linguagem))  # Formatação com % (antiga)