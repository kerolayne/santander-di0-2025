#modelos de chamadas de API
#         print(row)
#     else:
#         print("Nenhum dado encontrado com o ID:", id)
import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)
# Conexão com o banco de dados SQLite
def get_db_connection():
    conn = sqlite3.connect('example.db')
    conn.row_factory = sqlite3.Row
    return conn 

# Rota para inserir dados
@app.route('/insert', methods=['POST'])
def insert_data():
    data = request.get_json()
    name = data['name']
    age = data['age']
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO example (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify({'message': 'Data inserted successfully'}), 201

# Rota para consultar todos os dados
@app.route('/data', methods=['GET'])
def get_data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM example")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    
    return jsonify([dict(row) for row in rows]), 200
# Rota para consultar um dado específico
@app.route('/data/<int:id>', methods=['GET'])
def get_single_data(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM example WHERE id = ?", (id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    
    if row:
        return jsonify(dict(row)), 200
    else:
        return jsonify({'message': 'Data not found'}), 404
# Rota para atualizar dados
@app.route('/update/<int:id>', methods=['PUT'])
def update_data(id):
    data = request.get_json()
    name = data['name']
    age = data['age']
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE example SET name = ?, age = ? WHERE id = ?", (name, age, id))
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify({'message': 'Data updated successfully'}), 200
# Rota para deletar dados
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_data(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM example WHERE id = ?", (id,))
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify({'message': 'Data deleted successfully'}), 200
# Rota para inserir dados em lote
@app.route('/insert_batch', methods=['POST'])
def insert_batch():
    data = request.get_json()
    if not isinstance(data, list):
        return jsonify({'message': 'Invalid data format, expected a list'}), 400
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.executemany("INSERT INTO example (name, age) VALUES (?, ?)", [(item['name'], item['age']) for item in data])
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify({'message': 'Batch data inserted successfully'}), 201

# Função para iniciar o servidor Flask
def run_server():
    app.run(debug=True)
if __name__ == '__main__':
    run_server()    
# To run this code, ensure you have Flask installed in your Python environment.
# You can install it using pip:
# pip install Flask
# After running this script, you can access the API endpoints using a tool like Postman or curl.
# The database file 'example.db' will be created in the same directory as this script.