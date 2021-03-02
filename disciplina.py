import bd

colecao_disciplina = bd.get_colecao('disciplina')


def popula_disciplina():
    disciplinas = list()

    disciplinas.append({"nomeDisciplina": "Circuitos", "nomeProfessor": "Lucas Oliveira"})
    disciplinas.append({"nomeDisciplina": "Fisica 1", "nomeProfessor": "Fernanda Nodari"})
    disciplinas.append({"nomeDisciplina": "Calculo", "nomeProfessor": "Jose da Silva"})
    disciplinas.append({"nomeDisciplina": "Computacao 1", "nomeProfessor": "Jorge Habib"})
    disciplinas.append({"nomeDisciplina": "Estatistica", "nomeProfessor": "Carlos dos Santos"})
    disciplinas.append({"nomeDisciplina": "Engenharia de Software", "nomeProfessor": "Gil Brasil"})

    colecao_disciplina.insert_many(disciplinas)


def create_disciplina(nome_disciplina, nome_professor):
    colecao_disciplina.insert_one({'nomeDisciplina': nome_disciplina, 'nomeProfessor': nome_professor})


def read_discipina_todos():
    return colecao_disciplina.find()


def read_disciplina(nome_disciplina):
    return colecao_disciplina.find_one({'nomeDisciplina': nome_disciplina})


def update_disciplina(nome_disciplina, propriedade, nova_prop):
    if propriedade == 'nomeDisciplina':
        colecao_disciplina.find_one_and_update({'nomeDisciplina': nome_disciplina}, {'$set': {'nomeDisciplina': nova_prop}})
    elif propriedade == 'nomeProfessor':
        colecao_disciplina.find_one_and_update({'nomeDisciplina': nome_disciplina}, {'$set': {'nomeProfessor': nova_prop}})


def delete_disciplina(nome_disciplina):
    colecao_disciplina.delete_one({'nomeDisciplina': nome_disciplina})