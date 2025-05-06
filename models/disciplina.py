import sqlite3

def criarUmaDisciplina(nome: str, codigo: str, professor_id: int, carga_horaria: int) -> str:
    """_summary_

    Args:
        nome (str): Nome da disciplina
        codigo (str): Código da disciplina
        professor_id (int): Id do professor
        carga_horaria (int): Carga horária da disciplina

    Returns:
        str: Retorna uma mensagem de sucesso
    """    
    conexao = sqlite3.connect("escola.db");
    
    conn = conexao.cursor()

    data = (nome, codigo, professor_id, carga_horaria)

    conn.execute("INSERT INTO disciplinas (nome, codigo, professor_id, carga_horaria) VALUES (?, ?, ?, ?)", data)

    conexao.commit()

    return f"Disciplina {nome} cadastrada com sucesso."

def disciplinasDisponiveis():
    conexao = sqlite3.connect("escola.db");
    
    conn = conexao.cursor()

    conn.execute("SELECT * FROM disciplinas")

    disciplinas = conn.fetchall()

    return disciplinas

def pesquisarDisciplina(disciplina_id: int):
    """_summary_

    Args:
        disciplina_id (int): Id da disciplina

    Returns:
        _type_: Retorna uma mensagem com os dados da disciplina encontrada
    """    
    conexao = sqlite3.connect("escola.db");
    
    conn = conexao.cursor()

    conn.execute(f"SELECT * FROM disciplinas WHERE id = {disciplina_id}")

    disciplina = conn.fetchone()

    return disciplina