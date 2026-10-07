# Formas reutilizadas pelos exemplos: cada função devolve (posições, cores).
# Todas são definidas em coordenadas LOCAIS, centradas na origem.


def seta(corCorpo=[1.0, 0.85, 0.2], corPonta=[1.0, 0.35, 0.15]):
    """Seta apontando para cima (+y). A ponta mostra a orientação do objeto."""
    posicoes = [
        # corpo: retângulo com dois triângulos
        [-0.05, -0.20, 0.0], [0.05, -0.20, 0.0], [0.05, 0.05, 0.0],
        [-0.05, -0.20, 0.0], [0.05, 0.05, 0.0], [-0.05, 0.05, 0.0],
        # ponta
        [-0.12, 0.05, 0.0], [0.12, 0.05, 0.0], [0.0, 0.20, 0.0],
    ]
    cores = [corCorpo] * 6 + [corPonta] * 3
    return posicoes, cores


def quadrado(corA, corB):
    """Quadrado de lado 2 (de -1 a 1). As duas metades têm cores diferentes
    para que a rotação seja visível."""
    posicoes = [
        [-1.0, -1.0, 0.0], [1.0, -1.0, 0.0], [1.0, 1.0, 0.0],
        [-1.0, -1.0, 0.0], [1.0, 1.0, 0.0], [-1.0, 1.0, 0.0],
    ]
    cores = [corA] * 3 + [corB] * 3
    return posicoes, cores


def eixos(tamanho=1.0):
    """Eixos X (vermelho) e Y (verde), desenhados com GL_LINES."""
    posicoes = [
        [-tamanho, 0.0, 0.0], [tamanho, 0.0, 0.0],
        [0.0, -tamanho, 0.0], [0.0, tamanho, 0.0],
    ]
    cores = [[0.85, 0.3, 0.3]] * 2 + [[0.3, 0.8, 0.35]] * 2
    return posicoes, cores
