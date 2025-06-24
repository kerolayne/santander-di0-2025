#como manipular arquivos em python 

file = open("arquivo.txt", "w")  # Abre o arquivo para escrita
file.write("Olá, mundo!\n")  # Escreve uma linha no arquivo
file.close()  # Fecha o arquivo
# Abre o arquivo para leitura
file = open("arquivo.txt", "r")
conteudo = file.read()  # Lê o conteúdo do arquivo
print(conteudo)  # Exibe o conteúdo lido
# Fecha o arquivo
file.close()

#aquivo .csv
import csv
with open("dados.csv", mode="w", newline="") as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow(["Nome", "Idade", "Cidade"])  # Cabeçalho
    escritor_csv.writerow(["Alice", 30, "São Paulo"])
    escritor_csv.writerow(["Bob", 25, "Rio de Janeiro"])
# Lendo o arquivo CSV
with open("dados.csv", mode="r") as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    for linha in leitor_csv:
        print(linha)
# Manipulando arquivos JSON
import json
dados = {
    "pessoas": [
        {"nome": "Alice", "idade": 30, "cidade": "São Paulo"},
        {"nome": "Bob", "idade": 25, "cidade": "Rio de Janeiro"}
    ]
}   
# Escrevendo dados em um arquivo JSON
with open("dados.json", "w") as arquivo_json:
    json.dump(dados, arquivo_json, indent=4)  # Escreve com indentação de 4 espaços
# Lendo dados de um arquivo JSON
with open("dados.json", "r") as arquivo_json:
    dados_lidos = json.load(arquivo_json)  # Lê o conteúdo do arquivo JSON
    print(dados_lidos)  # Exibe os dados lidos
# Manipulando arquivos binários
with open("dados.bin", "wb") as arquivo_binario:
    # Escrevendo dados binários
    arquivo_binario.write("Exemplo de dados binários\n".encode("utf-8"))
    arquivo_binario.write(b"1234567890")  # Escreve uma sequência de bytes
# Lendo dados de um arquivo binário
with open("dados.bin", "rb") as arquivo_binario:
    conteudo_binario = arquivo_binario.read()  # Lê o conteúdo do arquivo binário
    print(conteudo_binario)  # Exibe os dados lidos
    

