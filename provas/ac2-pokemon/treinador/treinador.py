from flask import Flask, request, jsonify
from to_dict import *
from validacao import *
from enum import Enum, auto

treinadores = {}

class Genero(Enum):
    FEMININO = auto()
    MASCULINO = auto()

    @staticmethod
    def decodificar(valor):
        for g in Genero:
            if g.name.lower() == valor:
                return g
        raise ValueError()

    def __str__(self):
        return self.name.lower()

class PokemonJaExisteException(Exception):
    pass

class Treinador:
    def __init__(self, nome):
        self.__nome = nome
        self.__pokemons = {}

    @property
    def nome(self):
        return self.__nome

    @property
    def pokemons(self):
        return self.__pokemons

    def adicionar_pokemon(self, apelido, tipo, experiencia, genero):
        if apelido in self.__pokemons: raise PokemonJaExisteException()
        self.__pokemons[apelido] = Pokemon(apelido, tipo, experiencia, genero)

class Pokemon:
    def __init__(self, apelido, tipo, experiencia, genero):
        self.__apelido = apelido
        self.__tipo = tipo
        self.__genero = genero
        self.__experiencia = experiencia

    @property
    def apelido(self):
        return self.__apelido

    @property
    def tipo(self):
        return self.__tipo

    @property
    def experiencia(self):
        return self.__experiencia

    @property
    def genero(self):
        return self.__genero

    def ganhar_experiencia(self, ganho):
        self.__experiencia += ganho

app = Flask(__name__)

@app.route("/pid")
def dar_pid():
    from os import getpid
    return str(getpid())

@app.route("/hello")
def hello():
    return "Pikachu, eu escolho você!"

@app.route("/reset", methods = ["POST"])
def reset():
    treinadores.clear()
    return "Equipe Rocket decolando na velocidade da luz!"

@app.route("/treinador")
def listar_treinadores():
    return jsonify(to_dict(treinadores))

@app.route("/treinador/<nome>")
def detalhar_treinador(nome):
    if nome not in treinadores: return "", 404
    return jsonify(to_dict(treinadores[nome]))

@app.route("/treinador/<nome>/<apelido>")
def detalhar_pokemon(nome, apelido):
    if nome not in treinadores: return "Treinador não existe.", 404
    treinador = treinadores[nome]
    pokemons = treinador.pokemons
    if apelido not in pokemons: return "Pokémon não existe.", 404
    return jsonify(to_dict(pokemons[apelido]))

@app.route("/treinador/<nome>", methods = ["PUT"])
def cadastrar_treinador(nome):
    if nome in treinadores: return jsonify(to_dict(treinadores[nome])), 303
    t = Treinador(nome)
    treinadores[nome] = t
    return jsonify(to_dict(t)), 202

@app.route("/treinador/<nome>", methods = ["DELETE"])
def excluir_treinador(nome):
    if nome not in treinadores: return "", 404
    del treinadores[nome]
    return "", 204

def str_genero(valor):
    return valor in ['feminino', 'masculino']

@app.route("/treinador/<nome>/<apelido>", methods = ["PUT"])
def cadastrar_pokemon(nome, apelido):
    if nome not in treinadores: return "", 404
    treinador = treinadores[nome]
    pokemons = treinador.pokemons
    if apelido in pokemons: return "", 409
    dados = request.get_json()
    validar_campos(dados, {'tipo': str_nao_vazio, 'experiencia': natural, 'genero': str_genero})
    pokemon = treinador.adicionar_pokemon(apelido, dados['tipo'], dados['experiencia'], Genero.decodificar(dados['genero']))
    return jsonify(to_dict(pokemon)), 202

@app.route("/treinador/<nome>/<apelido>/exp", methods = ["POST"])
def adicionar_experiencia(nome, apelido):
    if nome not in treinadores: return "Treinador não existe.", 404
    treinador = treinadores[nome]
    pokemons = treinador.pokemons
    if apelido not in pokemons: return "Pokémon não existe.", 404
    pokemon = pokemons[apelido]
    dados = request.get_json()
    validar_campos(dados, {'experiencia': natural})
    pokemon.ganhar_experiencia(dados['experiencia'])
    return "", 204

@app.route("/treinador/<nome>/<apelido>", methods = ["DELETE"])
def excluir_pokemon(nome, apelido):
    if nome not in treinadores: return "Treinador não existe.", 404
    treinador = treinadores[nome]
    pokemons = treinador.pokemons
    if apelido not in pokemons: return "Pokémon não existe.", 404
    del pokemons[apelido]
    return "", 204

if __name__ == "__main__":
    app.run(port = 9000)