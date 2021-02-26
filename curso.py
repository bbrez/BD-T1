from pymongo import MongoClient, ReturnDocument

cliente = MongoClient()
bd = cliente['bd3']
colecao_cursos = bd['curso']


def popula_curso():
    lista_cursos = list()
    lista_cursos.append({'nomeCurso': 'Engenharia Elétrica'})
    lista_cursos.append({'nomeCurso': 'Ciência da Computação'})

    colecao_cursos.insert_many(lista_cursos)


def insere_curso(nome_curso):
    colecao_cursos.insert_one({'nomeCurso': nome_curso})
    return 'inserido curso {}'.format(nome_curso)


def procura_curso_todos():
    return colecao_cursos.find()


def procura_curso(nome_curso):
    return colecao_cursos.find_one({'nomeCurso': nome_curso})


def remove_curso(nome_curso):
    colecao_cursos.delete_one({'nomeCurso': nome_curso})
    return 'deletado curso {}'.format(nome_curso)


def atualiza_curso(nome_curso, novo_nome):
    return colecao_cursos.find_one_and_update({'nomeCurso': nome_curso}, {'$set': {'nomeCurso': novo_nome}},
                                              return_document=ReturnDocument.AFTER)
