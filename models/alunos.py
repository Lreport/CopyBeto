
import sqlite3

def criarUmAluno(nome: str, matricula: str, data_nascimento: str, sexo: str, endereco: str, telefone: str, email: str) -> str:
   """_summary_

   Args:
       nome (str): Nome do aluno
       matricula (str): Matricula do aluno
       data_nascimento (str): Data de nascimento do aluno
       sexo (str): Sexo do aluno
       endereco (str): Endereço do aluno
       telefone (str): Telefone do aluno
       email (str): Email do aluno

   Returns:
       str: Retorna uma mensagem de sucesso
   """   
   conexao = sqlite3.connect("escola.db");
    
   conn = conexao.cursor()

   data = (nome, matricula, data_nascimento, sexo, endereco, telefone, email)

   conn.execute("INSERT INTO alunos(nome, matricula, data_nascimento, sexo, endereco, telefone, email) VALUES (?, ?, ?, ?, ?, ?, ?)", data)

   conexao.commit()

   return f"Aluno {nome} cadastro com sucesso.\n N° matricula: {matricula}"

def pesquisarAlunos(id: int):
   """_summary_

   Args:
       id (int): Id do aluno

   Returns:
       _type_: Retorna uma mensagem com os dados do aluno encontrado
   """   
   conexao = sqlite3.connect("escola.db")

   conn = conexao.cursor()

   alunos = conn.execute(f"SELECT * FROM alunos WHERE id = {id}")

   aluno = alunos.fetchone()

   return aluno

def alunosDisponiveis() -> str:
   """_summary_

   Returns:
       str: Retorna uma mensagem com os dados dos alunos disponíveis
   """   
   conexao = sqlite3.connect("escola.db")

   conn = conexao.cursor()

   alunos = conn.execute("SELECT * FROM alunos")

   alunos = alunos.fetchall()

   return alunos