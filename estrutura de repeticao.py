texto = "Olá, mundo!"	

for i in texto:
    print(i)    

while texto:
    print(texto[0])  # Imprime o primeiro caractere
    texto = texto[1:]  # Remove o primeiro caractere