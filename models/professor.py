import sqlite3

def criarUmProfessor(nome: str, codigo: str, data_nascimento: str, sexo: str, endereco: str, telefone: str, email: str) -> str:
   """_summary_

   Args:
       nome (str): Nome do Professor
       codigo (str): Código do Professor
       data_nascimento (str): Data de Nascimento do Professor
       sexo (str): Sexo do Professor
       endereco (str): Endereço do Professor
       telefone (str): Telefone do Professor
       email (str): Email do Professor

   Returns:
       str: Retorna uma mensagem de sucesso
   """
   conexao = sqlite3.connect("escola.db");
    
   conn = conexao.cursor()

   data = (nome, codigo, data_nascimento, sexo, endereco, telefone, email)

   conn.execute("INSERT INTO professores(nome, codigo, data_nascimento, sexo, endereco, telefone, email) VALUES (?, ?, ?, ?, ?, ?, ?)", data)

   conexao.commit()

   return f"Aluno {nome} cadastro com sucesso.\n N° codigo: {codigo}"

def professoresDisponiveis() -> str:
   conexao = sqlite3.connect("escola.db")

   conn = conexao.cursor()

   professores = conn.execute("SELECT * FROM professores")

   professores = professores.fetchall()

   return professores

def pesquisarUmProfessor(id: int) -> str:
   """_summary_

   Args:
       id (int): Id do Professor

   Returns:
       str: Retorna uma mensagem com os dados do professor encontrado
   """   
   conexao = sqlite3.connect("escola.db")

   conn = conexao.cursor()

   professores = conn.execute(f"""
    SELECT professores.*, disciplinas.*
    FROM professores
    LEFT JOIN disciplinas ON professores.id = disciplinas.professor_id
    WHERE professores.id = {id}
   """)

   professor = professores.fetchone()

   return professor

def pesquisarDisciplinaDoProfessor(id: int) -> str:
   """_summary_

   Args:
       id (int): Id do Professor

   Returns:
       str: Retorna uma mensagem com as disciplinas do professor encontrado
   """   
   conexao = sqlite3.connect("escola.db")

   conn = conexao.cursor()

   disciplinas = conn.execute(f"""
      SELECT * 
                              FROM disciplinas
                              LEFT JOIN professores ON professores.id = disciplinas.professor_id
                              WHERE professores.id = {id}
   """)

   disciplina = disciplinas.fetchall()

   return disciplina