import sqlite3

def cadastrarDisciplinaEmTurma(turma_id: int, disciplina_id: int) -> str:
    """_summary_

    Args:
        turma_id (int): Id da Turma
        disciplina_id (int): Id da Disciplina

    Returns:
        str: Retorna uma mensagem de sucesso
    """    
    conexao = sqlite3.connect("escola.db");

    conn = conexao.cursor()

    data = (turma_id, disciplina_id)

    conn.execute("INSERT INTO turmas_disciplinas (turma_id, disciplina_id) VALUES (?, ?)", data)

    conexao.commit()

    return f"Disciplina cadastrada com sucesso na turma."

def disciplinasEmUmaTurma(turma_id: int):
    """_summary_

    Args:
        turma_id (int): Id da Turma

    Returns:
        _type_: Retorna uma mensagem com as disciplinas da turma
    """    
    conexao = sqlite3.connect("escola.db");

    conn = conexao.cursor()

    data = (turma_id,)

    conn.execute("""
    SELECT disciplinas.nome, disciplinas.codigo
    FROM turmas_disciplinas
    LEFT JOIN turmas ON turmas.id = turmas_disciplinas.turma_id
    LEFT JOIN disciplinas ON disciplinas.id = turmas_disciplinas.disciplina_id
    WHERE turmas_disciplinas.turma_id = ?
    """, data)

    disciplinas = conn.fetchall()

    return disciplinas