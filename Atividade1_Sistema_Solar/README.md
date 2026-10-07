# Aula de Transformações Geométricas: Python e OpenGL
Prof. Rodrigo Fernandes dos Santos. Computação Gráfica, Unipac Barbacena.

## Ambiente
Python 3.11 a 3.13, Pygame 2.6.1, PyOpenGL 3.1.10 e NumPy 1.26 ou 2.x.
A placa de vídeo precisa oferecer OpenGL 3.3 core.

## Windows (PowerShell)
Abra o terminal na pasta `alunos`.
```powershell
py -3 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe demo1_matrizes.py
.venv\Scripts\python.exe demo2_transformacoes.py
.venv\Scripts\python.exe demo3_global_local.py
```

## macOS (Terminal)
Abra o terminal na pasta `alunos`.
```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python demo1_matrizes.py
.venv/bin/python demo2_transformacoes.py
.venv/bin/python demo3_global_local.py
```

No PyCharm, abra a pasta `alunos` como projeto e execute cada arquivo com **Run**.

ESC fecha a janela. P salva a captura em `capturas/resultado.png`.

## Demonstrações
| Arquivo | O que mostra | Teclas |
|---|---|---|
| `demo1_matrizes.py` | Matrizes 4x4 aplicadas a um ponto, no terminal, sem janela | — |
| `demo2_transformacoes.py` | Translação, rotação, escala e a diferença entre `T @ R` e `R @ T` | 1 a 6 |
| `demo3_global_local.py` | Transformações globais e locais, perspectiva e ortográfica | WASD ZX QE (global), IJKL UO (local), V (projeção), R (reinicia) |

## Organização
- `core/`: `Base`, `Input`, `Utils` (shaders), `Attribute`, `Uniform` (com `mat4`) e `Matrix`.
- `formas.py`: seta, quadrado e eixos em coordenadas locais.
- `objeto.py`: um VAO por objeto, desenhado com `desenhar()`.
- `shaders.py`: `gl_Position = projectionMatrix * modelMatrix * vec4(position, 1.0)`.
- `atividade_sistema_solar.py`: arquivo inicial da atividade (veja `ATIVIDADE.md`).

## Convenções
- As matrizes do NumPy estão por linhas. `Uniform` envia `mat4` com `GL_TRUE` (transpor), pois o GLSL guarda as matrizes por colunas.
- Em `A @ B @ ponto`, a matriz mais à direita é aplicada primeiro.
- Transformação **global** (eixos do mundo): `m @ modelo`. Transformação **local** (eixos do objeto): `modelo @ m`.
- Velocidades em unidades ou radianos **por segundo**, multiplicadas por `self.deltaTime`.

## Problemas comuns
- Tela preta com perspectiva: o objeto está em z = 0. A câmera olha para -z e o plano *near* é 0.1. Translade para z = -1.
- Objeto distorcido ou sumido: a matriz foi enviada sem transpor, ou o tipo da `Uniform` não é `mat4`.
- O objeto gira "em volta do mundo" em vez de girar no lugar: a ordem está trocada (`R @ T` em vez de `T @ R`).
- `ModuleNotFoundError: core`: execute a partir da pasta `alunos`.

## Referência
STEMKOSKI, Lee; PASCALE, Michael. *Developing graphics frameworks with Python and OpenGL*. Boca Raton: CRC Press, 2022. Capítulo 3 (Matrix Algebra and Transformations).
