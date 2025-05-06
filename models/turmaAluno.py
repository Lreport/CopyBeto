import sqlite3

def matricularUmAlunoEmTurma(turma_id: int, aluno_id: int) -> str:
    """_summary_

    Args:
        turma_id (int): Id da Turma
        aluno_id (int): Id do Aluno

    Returns:
        str: Retorna uma mensagem de sucesso
    """    
    conexao = sqlite3.connect("escola.db");
    
    conn = conexao.cursor()

    data = (turma_id, aluno_id)

    conn.execute("INSERT INTO turmas_alunos (turma_id, aluno_id) VALUES (?, ?)", data)

    conexao.commit()

    return f"Aluno matriculado com sucesso."

def alunosMatriculadosEmUmaTurma(turma_id: int):
    """_summary_

    Args:
        turma_id (int): Id da Turma

    Returns:
        _type_: Retorna uma mensagem com os alunos matriculados na turma
    """    
    conexao = sqlite3.connect("escola.db");
    
    conn = conexao.cursor()

    data = (turma_id,)

    conn.execute("""
    SELECT alunos.nome, alunos.matricula
    FROM turmas_alunos
    LEFT JOIN turmas ON turmas.id = turmas_alunos.turma_id
    LEFT JOIN alunos ON alunos.id = turmas_alunos.aluno_id
    WHERE turmas_alunos.turma_id = ?
    """, data)

    alunos = conn.fetchall()

    return alunos