from flask import Flask, jsonify

app = Flask(__name__)

Esporte = [
        {'id': 1, 'nome': 'Futebol'},
        {'id': 2, 'nome': 'Basquete'},
        {'id': 3, 'nome': 'Futebol Americano'},
        {'id': 4, 'nome': 'Beisebol'},
    ]

@app.route('/Esporte', methods=['GET'])
def buscar():  
    return jsonify(Esporte, 201)

if __name__ == '_main_':
    app.run(debug=True, port=501)