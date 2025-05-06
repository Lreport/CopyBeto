from models.turma import criarUmaTurma, turmasDisponiveis, pesquisarTurma
from utils.codigo import gerarCodigoTurma
from models.aluno import alunosDisponiveis, pesquisarAlunos
from models.turmaAluno import matricularUmAlunoEmTurma, alunosMatriculadosEmUmaTurma
from models.disciplina import disciplinasDisponiveis, pesquisarDisciplina
from models.turmaDisciplina import cadastrarDisciplinaEmTurma, disciplinasEmUmaTurma

def criarTurma():
    """_summary_
    Cadastra uma turma
    Returns:
        _type_: Retorna uma mensagem de sucesso
    """    
    print('------------ TURMAS ------------')
    print('\n Bem vindo ao servidor de cadastro de turmas \n')

    nome = str(input("Digite o nome da turma para começar:\n"))

    codigo = gerarCodigoTurma()

    criarUmaTurma(nome, codigo)

    return print(f"Turma {nome} cadastrada com sucesso.\n N° codigo: {codigo}");

def matricularAlunoEmTurma():
    """_summary_
    Matricula um aluno em uma turma
    Returns:
        _type_: Retorna uma mensagem de sucesso
    """    
    print('------------ MATRICULAS ------------')
    print('\n Bem vindo ao servidor de matricula de alunos \n')

    alunos = alunosDisponiveis()

    for i in range(0, len(alunos)):
        print(f"Id: {alunos[i][0]} - Nome: {alunos[i][1]}")
    
    aluno = int(input("Qual o id do aluno que deseja matricular?\n"))

    alunoPesquisado = pesquisarAlunos(aluno)

    if not alunoPesquisado:
        print('Error: aluno não encontrado')
        exit()

    turmas = turmasDisponiveis()

    for i in range(0, len(turmas)):
        print(f"Id: {turmas[i][0]} - Nome: {turmas[i][1]}")

    turma = int(input("Qual o id da turma que deseja matricular o aluno?\n"))

    turmaPesquisada = pesquisarTurma(turma)

    if not turmaPesquisada:
        print('Error: turma não encontrada')
        exit()
    
    matricularUmAlunoEmTurma(aluno, turma)

    return print(f"Aluno {alunoPesquisado[1]} matriculado com sucesso na turma {turmaPesquisada[1]}.\n");


def alunosMatriculadosEmTurma():
    """_summary_
    Mostra os alunos matriculados em uma turma
    Returns:
        _type_: Retorna uma mensagem com os alunos matriculados em uma turma
    """    
    turmas = turmasDisponiveis()

    for i in range(0, len(turmas)):
        print(f"Id: {turmas[i][0]} - Nome: {turmas[i][1]}")
    
    turma = int(input("Qual o id da turma que deseja ver os alunos matriculados?\n"))

    turmaPesquisada = pesquisarTurma(turma)

    if not turmaPesquisada:
        print('Error: turma não encontrada')
        exit()
    
    alunos = alunosMatriculadosEmUmaTurma(turma)

    if not alunos:
        print('Nenhum aluno matriculado nessa turma')
        exit()
    
    for i in range(0, len(alunos)):
        print(f"Nome: {alunos[i][0]} - Matricula: {alunos[i][1]}")

    return print(f"Alunos matriculados na turma {turmaPesquisada[1]}.\n");

def cadastrarDisciplinaNaTurma():
    """_summary_
    Cadastra uma disciplina em uma turma
    Returns:
        _type_: Retorna uma mensagem de sucesso
    """    
    print('------------ DISCIPLINAS ------------')
    print('\n Bem vindo ao servidor de cadastro de disciplinas em turmas \n')

    disciplinas = disciplinasDisponiveis()

    for i in range(0, len(disciplinas)):
        print(f"Id: {disciplinas[i][0]} - Nome: {disciplinas[i][1]}")
    
    disciplina = int(input("Qual o id da disciplina que deseja cadastrar na turma?\n"))

    disciplinaPesquisada = pesquisarDisciplina(disciplina)

    if not disciplinaPesquisada:
        print('Error: disciplina não encontrada')
        exit()

    turmas = turmasDisponiveis()

    for i in range(0, len(turmas)):
        print(f"Id: {turmas[i][0]} - Nome: {turmas[i][1]}")

    turma = int(input("Qual o id da turma que deseja cadastrar a disciplina?\n"))

    turmaPesquisada = pesquisarTurma(turma)

    if not turmaPesquisada:
        print('Error: turma não encontrada')
        exit()
    
    cadastrarDisciplinaEmTurma(disciplina, turma)

    return print(f"Disciplina {disciplinaPesquisada[1]} cadastrada com sucesso na turma {turmaPesquisada[1]}.\n");


def disciplinasCadastradasEmUmaTurma():
    """_summary_
    Mostra as disciplinas cadastradas em uma turma
    Returns:
        _type_: Retorna uma mensagem com as disciplinas cadastradas em uma turma
    """    
    turmas = turmasDisponiveis()

    for i in range(0, len(turmas)):
        print(f"Id: {turmas[i][0]} - Nome: {turmas[i][1]}")
    
    turma = int(input("Qual o id da turma que deseja ver as disciplinas cadastradas?\n"))

    turmaPesquisada = pesquisarTurma(turma)

    if not turmaPesquisada:
        print('Error: turma não encontrada')
        exit()
    
    disciplinas = disciplinasEmUmaTurma(turma)

    if not disciplinas:
        print('Nenhuma disciplina cadastrada nessa turma')
        exit()
    
    for i in range(0, len(disciplinas)):
        print(f"Nome: {disciplinas[i][0]} - Código: {disciplinas[i][1]}")

    return print(f"Disciplinas cadastradas na turma {turmaPesquisada[1]}.\n");