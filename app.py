from flask import Flask,request, jsonify, render_template

app = Flask(__name__)
database = {}
database["ALUNO"] = []
database["PROFESSOR"] = []

@app.route("/s")

def index_simples():
   return "<h1> Carregando a minha primeira página </h1>" 

@app.route("/teste")

def teste():
    return  "<h1> Teste </h1>" 

@app.route("/user/<name>")

def user(name):
    return "<h1> Hello, {}!</h1>" .format(name)

@app.route("/alunos")

def listar_alunos():
    return jsonify(database["ALUNO"])


@app.route("/alunos", methods =["POST"])

def aluno_novo():
    novo_aluno = request.json
    database["ALUNO"].append(novo_aluno)
    return jsonify(database["ALUNO"])

@app.route('/alunos/<int:id_aluno>', methods=['GET'])

def localiza_aluno(id_aluno):

    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            return jsonify(aluno)

    return 'nao achei', 404

@app.route("/professor")

def listar_professores():
    return jsonify(database["PROFESSOR"])

@app.route("/professor", methods =["POST"])

def prof_novo():
    novo_prof = request.json
    database["PROFESSOR"].append(novo_prof)
    return jsonify(database["PROFESSOR"])

@app.route("/show_all")

def all():
    return jsonify(database) 

@app.route("/reseta", methods =["GET"])

def reseta():
    database["ALUNO"] = []
    database["PROFESSOR"] = []
    return jsonify(database)

@app.route("/")

def index():
    return render_template("index.html"), 200

@app.route("/usuario/<name>")

def usuario(name):
    return render_template("index.html", name=name), 200

if __name__ == '__main__':
    app.run()