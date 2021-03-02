import bd
import curso
import disciplina
from pprint import pprint


def menu_cursos():
    running = True
    while running:
        print('1 - Adicionar Curso')
        print('2 - Procurar Curso')
        print('3 - Atualizar Curso')
        print('4 - Remover Curso')
        print('5 - Adicionar Disciplina a Curso')
        print('6- Remover Disciplina de Curso')


def menu_principal():
    running = True
    while running:
        print('1 - Menu Cursos')
        print('2 - Menu Disciplinas')
        print('0 - Sair')
        opc = input('Opc Selecionada: ')

        if opc == 1:
            pass
        elif opc == 2:
            pass
        elif opc == 0:
            quit(0)
        else:
            print('Opção não encontrada')


if __name__ == '__main__':
    bd.clear_bd()
    disciplina.popula_disciplina()
    curso.popula_curso()
    curso.add_disciplina_curso('Ciência da Computação', 'Computaçao 1')
    curso.add_disciplina_curso('Ciência da Computação', 'Circuitos')
    pprint(curso.read_curso('Ciência da Computação'), sort_dicts=False)