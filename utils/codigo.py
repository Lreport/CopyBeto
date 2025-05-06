import random

def gerarCodigoProfessor() -> str:
    """_summary_

    Returns:
        str: Retorna um código gerado aleatoriamente
    """    
    letrasAlfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    numero = random.randint(1, 99999);
    letra = random.choice(letrasAlfabeto)

    return f"{letra}{numero}"

def gerarCodigoDisciplina() -> str:
    """_summary_

    Returns:
        str: Retorna um código gerado aleatoriamente
    """    
    letrasAlfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    numero = random.randint(1, 99999);
    letra = random.choice(letrasAlfabeto)

    return f"{letra}{numero}"


def gerarCodigoTurma() -> str:
    """_summary_

    Returns:
        str: Retorna um código gerado aleatoriamente
    """    
    letrasAlfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    numero = random.randint(1, 99999);
    letra = random.choice(letrasAlfabeto)

    return f"{letra}{numero}"