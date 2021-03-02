import bd
import curso
import disciplina
from pprint import pprint


def menu_disciplinas():
    running = True
    while running:
        print('1 - Adicionar Disciplina')
        print('2 - Procurar Disciplina')
        print('3 - Ver Todas Disciplinas')
        print('4 - Atualizar Disciplina')
        print('5 - Remover Disciplina')
        print('0 - Retornar')
        opc = input('Opc Selecionada: ')

        if opc == 1:
            disciplina.create_disciplina(input('Nome Disciplina: '), input('Nome Professor: '))

        elif opc == 2:
            pprint(disciplina.read_disciplina(input('Nome Disciplina: ')))

        elif opc == 3:
            pprint(disciplina.read_discipina_todos())

        elif opc == 4:
            print('Atualizar:')
            print('1 - Nome')
            print('2 - Professor')
            prop = input('Opc Selecionada: ')

            if prop == 1:
                disciplina.update_disciplina(input('Nome Disciplina: '), 'nomeDisciplina', input('Novo Nome: '))
            elif prop == 2:
                disciplina.update_disciplina(input('Nome Disciplina: '), 'nomeProfessor', input('Novo Professor: '))
            else:
                print('Erro')

        elif opc == 5:
            disciplina.delete_disciplina(input('Nome Disciplina'))

        elif opc == 0:
            running = False
        else:
            print('Opção não encontrada')


def menu_cursos():
    running = True
    while running:
        print('1 - Adicionar Curso')
        print('2 - Procurar Curso')
        print('3 - Ver todos os Cursos')
        print('4 - Atualizar Curso')
        print('5 - Remover Curso')
        print('6 - Adicionar Disciplina a Curso')
        print('7- Remover Disciplina de Curso')
        print('0 - Retornar')
        opc = input('Opc Selecionada: ')

        if opc == 1:
            nome_curso = input('Nome Curso: ')
            lista_disciplinas = [x.strip() for x in input('Disciplinas (separado por virgula): ').split(',')]
            curso.create_curso(nome_curso, lista_disciplinas)

        elif opc == 2:
            pprint(curso.read_curso(input('Nome Curso: ')))

        elif opc == 3:
            pprint(curso.read_curso_todos())

        elif opc == 4:
            curso.update_curso(input('Nome Curso: '), input('Novo nome: '))

        elif opc == 5:
            curso.delete_curso(input('Nome Curso: '))

        elif opc == 6:
            if not curso.add_disciplina_curso(input('Nome Curso: '), input('Nome Disciplina: ')):
                print('Disciplina nao encontrada')

        elif opc == 7:
            curso.remove_disciplina_curso(input('Nome Curso: '), input('Nome Disciplina: '))

        elif opc == 0:
            running = False
        else:
            print('Opção não encontrada')


def menu_principal():
    running = True
    while running:
        print('1 - Menu Cursos')
        print('2 - Menu Disciplinas')
        print('0 - Sair')
        opc = input('Opc Selecionada: ')

        if opc == 1:
            menu_cursos()
        elif opc == 2:
            menu_disciplinas()
        elif opc == 0:
            running = False
        else:
            print('Opção não encontrada')


if __name__ == '__main__':
    bd.clear_bd()
    disciplina.popula_disciplina()
    curso.popula_curso()
    curso.add_disciplina_curso('Ciência da Computação', 'Computaçao 1')
    curso.add_disciplina_curso('Ciência da Computação', 'Circuitos')
    pprint(curso.read_curso('Ciência da Computação'), sort_dicts=False)