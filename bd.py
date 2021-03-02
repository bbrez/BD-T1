from pymongo import MongoClient

conexao = MongoClient()['bd3']


def get_colecao(nome_colecao: str):
    return conexao[nome_colecao]


def clear_bd():
    conexao.drop_collection('disciplina')
    conexao.drop_collection('curso')