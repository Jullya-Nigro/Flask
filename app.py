from flask import Flask, request, jsonify # type: ignore

class CreateUser:
    id_counter = 0
    list_users = []
    def __init__(self, name, email, password):
        CreateUser.id_counter += 1   
        self.user = {
            "id": CreateUser.id_counter,
            "name": name,
            "email": email,
            "password": password
        }
        CreateUser.list_users.append(self.user)

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/getusers/", methods=['GET'])
def get_users():
    return jsonify(CreateUser.list_users),200

@app.route("/createusers/", methods=['POST'])
def create_users():
    data = request.get_json()
    user = CreateUser(data["name"], data["email"], data["password"])
    return jsonify(user.user)

@app.route("/users/<int:id>", methods=['PUT'])
def update_users(id):
    data = request.get_json()
    tipo = data.get("tipo")
    mudanca = data.get("mudanca")

    for i in CreateUser.list_users:
        if i["id"] == id:
            if tipo == "email" and mudanca != i["email"]:
                i["email"] = mudanca
                return jsonify(i)

            elif tipo == "password" and mudanca != i["password"]:
                i["password"] = mudanca
                return jsonify(i)

            else:
                return jsonify({"error": "Campo inválido ou valor igual ao anterior!"}), 400

    return jsonify({"error":"Usuário não encontrado!"}), 404

@app.route("/users/<int:id>", methods=['DELETE'])
def delete_users(id):
    for i in CreateUser.list_users:
        if i["id"] == id:
            CreateUser.list_users.remove(i)
            return jsonify({"msg": f"Usuário {id} removido com sucesso!"}), 200
    
    return jsonify({"error": "Usuário não encontrado!"}), 404
            

if __name__ == "__main__":
    app.run(debug=True, port=5001)

