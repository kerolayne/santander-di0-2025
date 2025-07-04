contatos = {
    "teste@gmail.com" : {"nome": "teste", "telefone": "123 456 789"}, 
    "contato@gmail.com" : {"nome":"contato", "telefone":"987 654 321"}, 
    "agente@gmail.com":{"nome": "agente", "telefone": "123 789 456"}
}

telefone = contatos["agente@gmail.com"]["telefone"]
print(telefone)

#for chave in contatos:
#    print(chave, contatos[chave])   

#print("=" * 100)

for chave, valor in contatos.items():
    print(chave, valor["nome"], valor["telefone"])

#dict é um tipo de dado que armazena pares chave-valor
# A chave é única e o valor pode ser qualquer tipo de dado

resultado = contatos.get("chave")
print(resultado)  # None, se a chave não existir

resultado = contatos.get("chave", {})
print(resultado)  # Retorna um dicionário vazio se a chave não existir

#keys
chaves = contatos.keys()
print(chaves)  # Retorna uma lista com as chaves do dicionário

#setdefault
resultado = contatos.setdefault("chave", {"nome": "valor", "telefone": "000 000 000"})
print(resultado)  # Retorna o valor associado à chave, ou o valor padrão se a chave não existir

#update
contatos.update({"chave": {"nome": "valor", "telefone": "000 000 000"}})   
print(contatos)  # Atualiza o dicionário com o novo par chave-valor
#pop
resultado = contatos.pop("chave", None)
print(resultado)  # Remove a chave e retorna o valor associado, ou None se a chave não existir
#popitem
resultado = contatos.popitem()
print(resultado)  # Remove e retorna o último par chave-valor adicionado ao dicionário
#clear
contatos.clear()  # Remove todos os itens do dicionário
#copy
copia_contatos = contatos.copy()  # Cria uma cópia superficial do dicionário
print(copia_contatos)  # Exibe a cópia do dicionário
#values
valores = contatos.values()  # Retorna uma lista com os valores do dicionário
print(valores)

