import sqlite3
from pathlib import Path
ROOT_PATH = Path(__file__).parent

con = sqlite3.connect('example.sqlite')
#print(con)

cur = con.cursor()


def criar_tabela():
    # Verifica se a tabela já existe e a remove se necessário
    cur.execute("DROP TABLE IF EXISTS example")
    # Cria a tabela
    cur.execute('''CREATE TABLE example
               (id INTEGER PRIMARY KEY AUTOINCREMENT,
               name varchar(100) NOT NULL,
               age INTEGER NOT NULL)''')

#inserir dados
def  inserir_dados(nome, idade):
    cur.execute("INSERT INTO example (name, age) VALUES (?, ?)", (nome, idade))

#inserir_dados("Alice", 30)
#nome = "Bob"
#idade = 25
#inserir_dados(nome, idade)
#commit as alterações
def commit_changes():
    con.commit()
commit_changes()

#consultar dados
def consultar_dados():
    cur.execute("SELECT * FROM example")
    rows = cur.fetchall()
    for row in rows:
        print(row)
#consultar_dados()
#fechar a conexão
def fechar_conexao():
    cur.close()



def atualizar_dados(con, cur, id, nome, idade):
    cur.execute("UPDATE example SET name =?, age =? WHERE id =?", (nome, idade, id))
    commit_changes()

def deletar_dados(con, cur, id):
    cur.execute("DELETE FROM example WHERE id = ?", (id,))
    commit_changes()
# Exemplo de uso das funções de atualização e deleção

atualizar_dados(con, cur, 1, "Alice", 31)
deletar_dados(con, cur, 2)
# Consultar novamente para verificar as alterações
#consultar_dados()

#inserir dados em lote
def inserir_dados_em_lote(dados):
    cur.executemany("INSERT INTO example (name, age) VALUES (?, ?)", dados)
    commit_changes()

# Exemplo de uso da função de inserção em lote
dados = [
    ("Charlie", 35),
    ("David", 40),
    ("Eva", 28)
]
inserir_dados_em_lote(dados)

# consultar somente um dado 

def consultar_um_dado(id):
    cur.execute("SELECT * FROM example WHERE id = ?", (id,))
    row = cur.fetchone()
    if row:
        print(row)
    else:
        print("Nenhum dado encontrado com o ID:", id)



#gerenciar transações

try:
    inserir_dados("Frank", 45)
    inserir_dados(2,"Grace", 50)
    commit_changes()
except Exception as exc:
    print("Erro ao inserir dados:", exc)
    con.rollback()

consultar_um_dado(1)
consultar_dados()
# Fechar a conexão ao final
fechar_conexao()