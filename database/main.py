import sqlite3

def criarBancoETabelas():
   """_summary_
   Cria o banco de dados e as tabelas
   """   
   conexao = sqlite3.connect("escola.db");
   
   conn = conexao.cursor()

   conn.execute("CREATE TABLE IF NOT EXISTS alunos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, matricula TEXT NOT NULL, data_nascimento DATE, sexo TEXT NOT NULL, endereco TEXT NOT NULL, telefone TEXT NOT NULL, email TEXT NOT NULL)")
   conn.execute("CREATE TABLE IF NOT EXISTS professores(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, codigo TEXT NOT NULL, data_nascimento DATE, sexo TEXT NOT NULL, endereco TEXT NOT NULL, telefone TEXT NOT NULL, email TEXT NOT NULL)")
   conn.execute("CREATE TABLE IF NOT EXISTS disciplinas(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, codigo, professor_id INTEGER NOT NULL, carga_horaria INTEGER NOT NULL, FOREIGN KEY (professor_id) REFERENCES professores (id))")
   conn.execute("CREATE TABLE IF NOT EXISTS turmas(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, codigo TEXT NOT NULL)")
   conn.execute("CREATE TABLE IF NOT EXISTS turmas_alunos(turma_id INTEGER NOT NULL, aluno_id INTEGER NOT NULL, FOREIGN KEY (turma_id) REFERENCES turmas (id), FOREIGN KEY (aluno_id) REFERENCES alunos (id))")
   conn.execute("CREATE TABLE IF NOT EXISTS turmas_disciplinas(turma_id INTEGER NOT NULL, disciplina_id INTEGER NOT NULL, FOREIGN KEY (turma_id) REFERENCES turmas (id), FOREIGN KEY (disciplina_id) REFERENCES disciplinas (id))")
   
   conexao.commit()
   conexao.close()