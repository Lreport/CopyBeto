from utils.formatador import formartarTelefone
from utils.matricula import gerarMatricula
from models.aluno import criarUmAluno
import sqlite3

def criarAluno():
    """_summary_

    Raises:
        SystemError: Erro no Sistema

    Returns:
        _type_: Retorna uma mensagem de sucesso
    """    
    print('------------ INFORMAÇÕES PESSOAIS ------------')
    print('\n Bem vindo ao servidor de cadastro do IFMS \n')

    nome = str(input("Digite o nome do aluno para começar:\n"))
    diaNascimento = int(input("Qual o dia de nascimento do aluno?\n"))

    if diaNascimento > 31:
        print('Error: digite um dia de nascimento válido')
        exit()
    
    mesNascimento = int(input("Qual o mês de nascimento do aluno? \n"))

    if mesNascimento > 12:
        print('Error: digite um mês de nascimento válido')
        exit()

    anoNascimento = int(input("Digite o ano de nascimento do aluno: ex: (2001) \n"))

    if(anoNascimento < 1900):
        print('Error: ano de nascimento inválido!')
        exit()

    dataNascimento = f"{diaNascimento}/{mesNascimento}/{anoNascimento}"

    sexoInput = str(input("Qual o sexo do aluno? (masculino) ou (feminino)\n"))

    sexo = "";

    if sexoInput != "masculino" and sexoInput != "Masculino" and sexoInput != "M" and sexoInput != "m" and sexoInput != "feminino" and sexoInput != "Feminino" and sexoInput != "F" and sexoInput != "f":
        print("Error: sexo do aluno inválido")
        exit()
    elif sexoInput == "masculino" or sexoInput == "Masculino" or sexoInput == "M" or sexoInput == "m":
        sexo = "M"
    elif sexoInput == "feminino" or sexoInput == "Feminino" or sexoInput == "F" or sexoInput == "f":
        sexo = "F"
    
    print("\n ---------- ENDEREÇO ----------\n\n")

    rua = str(input("Qual nome da rua que o aluno mora? Ex: (Manoel Pedro de Campos)\n"))
    bairro = str(input("Qual o bairro que o aluno mora? Ex: Santa Rita\n"))
    numero = str(input("Qual número da casa que o aluno mora? Ex: (1551)\n"))

    endereco = f"Rua {rua}, Bairro {bairro} - N° {numero}"


    print("\n ---------- Comunicação ---------- \n")

    telefoneInput = str(input("Digite o telefone do aluno: Ex: 6799999999 \n"))
    email = str(input("Digite o email do aluno: Ex: jonathan@ifms.edu.br \n"))

    telefone = formartarTelefone(telefoneInput);
    matricula = gerarMatricula();
    
    aluno = criarUmAluno(nome, matricula, dataNascimento, sexo, endereco, telefone, email)
    if not aluno:
        raise SystemError("Ops... Ocorreu um erro inesperado")
    
    return print(f"Aluno {nome} criado com sucesso! \n N° da matricula: {matricula}")

def pesquisarAluno(): 
    """_summary_
    Pesquisa um aluno
    """     
    print('------------ PESQUISAR ALUNO ------------')
    print('\n Bem vindo a Pesquisa de Alunos \n')
    nome = input("Digite o nome do aluno: ")
    conexao = sqlite3.connect("escola.db")
    conn = conexao.cursor()
    conn.execute("SELECT * FROM alunos WHERE nome = ?", (nome,))
    resultado = conn.fetchone()
    
    if resultado:
        if isinstance(resultado, (list, tuple)):
            print(f"Nome: {resultado[1]}, Matrrícula: {resultado[2]}")
        else:
            print("Resultado inesperado:", resultado)
    else:
        print("Aluno não encontrado.")
