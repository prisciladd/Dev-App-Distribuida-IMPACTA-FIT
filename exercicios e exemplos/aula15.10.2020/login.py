from flask import Flask, render_template, request

app = Flask(__name__)

usuarios = [
{'login': 'aluno1', 'senha': 'azul'},
{'login': 'aluno2', 'senha': 'vermelho'}
]

@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html", mensagem = "Entre no sistema")

@app.route("/form_teste", methods=["PUT", "POST"])
def form_teste():
    login = request.form["login"]
    senha = request.form["password"]
    for user in usuarios:
        if user['login'] == login and user['senha'] == senha:
            return render_template("login_ok.html", login = login)
    return render_template("login.html", mensagem = "Login inválido.")

if __name__ == '__main__':
    app.run(debug=True)
