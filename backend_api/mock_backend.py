from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Configuração de CORS completa
CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)
app.url_map.strict_slashes = False

# ROTA DE LOGIN
@app.route('/api/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS': return '', 200
    dados = request.json
    print(f"\n[LOGIN] Usuário: {dados.get('email')}")
    
    return jsonify({
        "status": "success",
        "access_token": "token-teste-123", # O front precisa desse token
        "user": {
            "id": "1",
            "name": "Rafael Diesel",
            "email": dados.get('email'),
            "role": "admin"
        }
    }), 200

# ROTA QUE O FRONT CHAMA LOGO APÓS O LOGIN (O que faltava!)
@app.route('/api/user/me', methods=['GET', 'OPTIONS'])
def get_me():
    if request.method == 'OPTIONS': return '', 200
    print("[GET] Enviando dados do perfil para o Dashboard...")
    
    # Retornamos os mesmos dados para o front "sentir" que está logado
    return jsonify({
        "id": "1",
        "name": "Rafael Diesel",
        "email": "1136090@atitus.edu.br",
        "plan": "Premium",
        "created_at": "2026-01-01"
    }), 200

# ROTA DE CADASTRO
@app.route('/api/register', methods=['POST', 'OPTIONS'])
def register():
    if request.method == 'OPTIONS': return '', 200
    print(f"\n[CADASTRO] Novo usuário: {request.json.get('email')}")
    return jsonify({"status": "success"}), 201

if __name__ == "__main__":
    print("\n" + "="*40)
    print("   SIMULADOR COM ROTA DE PERFIL ATIVA")
    print("   Aguardando login para liberar o App...")
    print("="*40)
    app.run(host='0.0.0.0', port=5000, debug=True)