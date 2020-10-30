from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cliente.db"
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgre://usuario:senha @banco:porta/database"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://dbimpacta:impacta#2020@dbimpacta.postgresql.dbaas.com.br:5432/dbimpacta" #banco remoto do prof
db = SQLAlchemy(app)

class Cliente(db.Model): #criação da tabela
    __tablename__ = "tbCliente" #altera nome da classe de Cliente para tbcliente
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True)
    comment = db.Column(db.String(120)) #cria coluna comment tipo string tamanho 120
    

    def __init__(self, name, comment):
        self.name = name
        self.comment = comment

@app.route("/")
def index():
    clientes = Cliente.query.all() #faz select * classe Cliente e guarda em clientes, conteudo de clientes vai para index.html no {for}
    return render_template("index.html", clientes=clientes) #chama index e passa objeto cliente vazio pois é a primeira chamada

@app.route("/add", methods=['GET','POST'])
def add():
    if request.method == 'POST':
        cliente = Cliente(
            request.form['nome'],
            request.form['comentario']) #pega o que ta escrito na caixa formulario
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route("/edit/<int:id>", methods=['GET','POST'])
def edit(id):
    cliente = Cliente.query.get(id)
    if request.method == 'POST':
        cliente.name = request.form['nome']
        cliente.comment = request.form['comentario']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', cliente=cliente)

@app.route("/delete/<int:id>")
def delete(id):
    cliente = Cliente.query.get(id)#busca pelo id
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)