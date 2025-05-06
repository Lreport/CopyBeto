from controllers.alunoscontroller import criarAluno, pesquisarAluno
from controllers.professorcontroller import criarProfessor, pesquisarProfessor, disciplinasDoProfessor
from controllers.disciplinacontroller import criarDisciplina, pesquisarDisciplina
from controllers.turmascontroller import criarTurma, matricularAlunoEmTurma, alunosMatriculadosEmTurma, cadastrarDisciplinaNaTurma, disciplinasCadastradasEmUmaTurma
from database.main import criarBancoETabelas

def dashboard(): 
    """_summary_
    Mostra todas as opções de administração
    """    
    print('------------ DASHBOARD ------------')
    print('\n Bem vindo ao servidor administrativo do IFMS \n OBS: SE FOR A SUA PRIMEIRA VEZ RODANDO TECLE O NÚMERO 0 PRIMEIRO PARA CRIAR AS TABELAS NO BANCO DE DADOS\n')

    while True:
        print('O que deseja fazer?\n')
        print('0 - Criar tabelas no banco de dados\n')
        print('1 - Cadastrar aluno\n')
        print('2 - Cadastrar professor\n')
        print('3 - Cadastrar disciplina\n')
        print('4 - Pesquisar Aluno\n')
        print('5 - Pesquisar Professor\n')
        print('6 - Pesquisar Disciplina\n')
        print('7 - Cadastrar Turma \n')
        print('8 - Matricular Aluno em Turma \n')
        print('9 - Alunos Cadastrados em Turma \n')
        print('10 - Cadastrar uma disciplina na turma \n')
        print('11 - Disciplinas cadastradas em uma turma \n')
        print('12 - Disciplinas de um professor \n')
        print('13 - Sair\n')

        opcao = int(input('Digite a opção desejada: '))

        try:
            if opcao == 0:
                criarBancoETabelas()
                break
            elif opcao == 1:
                criarAluno()
                break
            elif opcao == 2:
                criarProfessor()
                break
            elif opcao == 3:
                criarDisciplina()
                break
            elif opcao == 4:
                pesquisarAluno()
                break
            elif opcao == 5:
                pesquisarProfessor()
                break
            elif opcao == 6: 
                pesquisarDisciplina()
                break
            elif opcao == 7:
                criarTurma()
                break
            elif opcao == 8:
                matricularAlunoEmTurma()
                break
            elif opcao == 9:
                alunosMatriculadosEmTurma()
                break
            elif opcao == 10:
                cadastrarDisciplinaNaTurma()
            elif opcao == 11:
                disciplinasCadastradasEmUmaTurma()
                break
            elif opcao == 12:
                disciplinasDoProfessor()
                break
            elif opcao == 13:
                print('Encerrando o servidor administrativo do IFMS...')
                break
            else:
                print('Opção inválida. Tente novamente.\n')
        except ValueError:
            print('Valores inválidos. Tente novamente.\n')