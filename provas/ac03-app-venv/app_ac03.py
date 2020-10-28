from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://dbimpacta:impacta#2020@dbimpacta.postgresql.dbaas.com.br:5432/dbimpacta" 
db = SQLAlchemy(app)

class Cliente(db.Model):
    __tablename__ = "tbClienteSTADIA" 
    ra = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(50))
    logradouro = db.Column (db.String(50))
    numero = db.Column(db.String(5))
    cep = db.Column (db.String(10))
    complemento = db.Column (db.String(20))
    

    def __init__(self, nome, email, logradouro, numero, cep, complemento):
        self.nome = nome
        self.email = email
        self.logradouro = logradouro
        self.numero = numero
        self.cep = cep
        self.complemento = complemento

@app.route("/")
def index():
    clientes = Cliente.query.all() 
    return render_template("index_ac03.html", clientes=clientes)

@app.route("/add", methods=['GET','POST'])
def add():
    if request.method == 'POST':
        cliente = Cliente(
        request.form['nome'],
        request.form['email'],
        request.form['logradouro'],
        request.form['numero'],
        request.form['cep'],
        request.form['complemento'])
        
        db.session.add(cliente)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_ac03.html')

@app.route("/edit/<int:ra>", methods=['GET','POST'])
def edit(ra):
    cliente = Cliente.query.get(ra)
    if request.method == 'POST':
        cliente.nome = request.form['nome']
        cliente.email = request.form['email']
        cliente.logradouro = request.form['logradouro']
        cliente.numero = request.form['numero']
        cliente.cep = request.form['cep']
        cliente.complemento = request.form['complemento']

        db.session.commit()
        
        return redirect(url_for('index'))
    
    return render_template('edit_ac03.html', cliente=cliente)

@app.route("/delete/<int:ra>")
def delete(ra):
    cliente = Cliente.query.get(ra)
    db.session.delete(cliente)
    db.session.commit()
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)