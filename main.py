import curso

if __name__ == '__main__':
    print(curso.procura_curso('Engenharia Elétrica'))
    print(curso.insere_curso('Psicologia'))
    print(curso.atualiza_curso('Psicologia', 'Medicina'))
    print(curso.remove_curso('Medicina'))