import random

def gerarMatricula() -> str:
    """_summary_

    Returns:
        str: Retorna uma matrícula gerada aleatoriamente
    """      

    letrasAlfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    numero = random.randint(1, 99999);
    letra = random.choice(letrasAlfabeto)

    return f"{numero}-{letra}"