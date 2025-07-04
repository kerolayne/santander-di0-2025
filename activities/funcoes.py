#como criar funcoes em python
def saudacao(nome):
    """
    Função que recebe um nome e retorna uma saudação personalizada.
    
    Args:
        nome (str): O nome da pessoa a ser saudada.
        
    Returns:
        str: Uma mensagem de saudação personalizada.
    """
    return f"Olá, {nome}! Seja bem-vindo(a)!"

saudacao_resultado = saudacao("João")
print(saudacao_resultado)  # Exibe a saudação personalizada

