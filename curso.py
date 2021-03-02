import bd
import disciplina

colecao_cursos = bd.get_colecao('curso')

def popula_curso():
    lista_cursos = list()
    lista_cursos.append({'nomeCurso': 'Engenharia Eletrica', 'disciplinas': ['Circuitos', 'Fisica 1', 'Calculo']})
    lista_cursos.append({'nomeCurso': 'Computacao', 'disciplinas': ['Computacao 1', 'Estatistica', 'Engenharia de Software']})

    colecao_cursos.insert_many(lista_cursos)


def create_curso(nome_curso, disciplinas):
    colecao_cursos.insert_one({'nomeCurso': nome_curso, 'disciplinas': disciplinas})


def read_curso_todos():
    return colecao_cursos.find()


def read_curso(nome_curso):
    curso = colecao_cursos.find_one({'nomeCurso': nome_curso})
    disciplinas = curso['disciplinas']
    del curso['disciplinas']
    curso['disciplinas'] = list()
    for disc in disciplinas:
        curso['disciplinas'].append(disciplina.read_disciplina(disc))
    return curso


def update_curso(nome_curso, novo_nome):
    colecao_cursos.find_one_and_update({'nomeCurso': nome_curso}, {'$set': {'nomeCurso': novo_nome}})


def delete_curso(nome_curso):
    colecao_cursos.delete_one({'nomeCurso': nome_curso})


def add_disciplina_curso(nome_curso, nome_disciplina):
    colecao_cursos.find_one_and_update({'nomeCurso': nome_curso}, {'$push': {'disciplinas': nome_disciplina}})


def remove_disciplina_curso(nome_curso, nome_disciplina):
    colecao_cursos.find_one_and_update({'nomeCurso': nome_curso}, {'$pull': {'disciplinas': nome_disciplina}})
