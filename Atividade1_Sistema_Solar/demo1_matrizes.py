# Demonstração 1 (sem janela): matrizes 4x4 aplicadas a um ponto com numpy.
# Execute e acompanhe a saída no terminal.
from math import pi

import numpy as np

from core.matrix import Matrix

np.set_printoptions(precision=2, suppress=True)

# ponto em coordenadas homogêneas: (x, y, z, 1)
ponto = np.array([0.5, 0.0, 0.0, 1.0])
print("Ponto original:", ponto)

T = Matrix.make_translation(0.0, 0.3, 0.0)
R = Matrix.make_rotation_z(pi / 2)  # 90 graus no sentido anti-horário
S = Matrix.make_scale(2.0)

print("\nMatriz de translação T(0, 0.3, 0):\n", T)
print("T @ ponto =", T @ ponto)

print("\nMatriz de rotação Rz(90°):\n", R)
print("R @ ponto =", R @ ponto)

print("\nMatriz de escala S(2):\n", S)
print("S @ ponto =", S @ ponto)

# A ORDEM IMPORTA: a matriz mais à direita é aplicada primeiro
print("\n--- Composição ---")
print("(T @ R) @ ponto  -> primeiro gira, depois translada:", (T @ R) @ ponto)
print("(R @ T) @ ponto  -> primeiro translada, depois gira:", (R @ T) @ ponto)

# Vetores (w = 0) não são afetados pela translação
vetor = np.array([0.5, 0.0, 0.0, 0.0])
print("\nVetor (w = 0):", vetor, "-> T @ vetor =", T @ vetor)
