from models.professor import professoresDisponiveis
from models.professor import pesquisarUmProfessor
from models.disciplina import criarUmaDisciplina
from utils.codigo import gerarCodigoDisciplina
import sqlite3

def criarDisciplina():
    """_summary_
    Cria uma disciplina
    Returns:
      _type_: Retorna uma mensagem com os dados da disciplina criada
    """    


    print('------------ DISCIPLINAS ------------')
    print('\n Bem vindo ao servidor de cadastro de disciplinas \n')

    nome = str(input("Digite o nome da disciplina para comecar:\n"))

    todosProfessores = professoresDisponiveis()

    professores = []

    for i in range(0, len(todosProfessores)):
      professores.append({ 'id': todosProfessores[i][0], 'nome': todosProfessores[i][1] })

    print("Professores disponiveis no IFMS:\n")
    print("Modelo de impressão: [numero] - [nome]\n")
    for i in range(0, len(professores)):
      print(f"{professores[i]['id']} - {professores[i]['nome']}")

    professor = int(input("Qual o numero do professor da disciplina?\n"))

    professorPesquisado = pesquisarUmProfessor(professor)

    if(professorPesquisado == None):
        print('Error: professor não encontrado')
        exit()

    cargaHoraria = int(input("Qual a carga horária da disciplina?\n"))

    codigo = gerarCodigoDisciplina()

    disciplina = criarUmaDisciplina(nome, codigo, professor, cargaHoraria);

    return print(disciplina);

def pesquisarDisciplina():
    """_summary_
    Pesquisa uma disciplina
    """    
    print('------------ DISCIPLINAS ------------')
    print('\n Bem vindo a Pesquisa de Disciplinas \n')

    disciplina = input("Digite o nome da disciplina: ")
    conexao = sqlite3.connect("escola.db")
    conn = conexao.cursor()
    conn.execute("SELECT * FROM disciplinas WHERE nome = ?", (disciplina,))
    resultado = conn.fetchone()

    if resultado:
        print("Disciplina foi encontrada:")
        for disciplina in resultado:
            print(f"Nome: {disciplina[1]}, Professor: {disciplina[2]}, Carga Horária: {disciplina[3]}")
    else:
        print("Disciplina nao encontrada.");