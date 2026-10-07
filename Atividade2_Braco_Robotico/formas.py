from core.mesh import Mesh
from geometry.boxGeometry import BoxGeometry
from material.basicMaterial import BasicMaterial

# tons de cinza por face simulam iluminação (ainda não temos luzes)
SOMBRA = [[0.85] * 3, [0.55] * 3, [1.0] * 3, [0.4] * 3, [0.7] * 3, [0.6] * 3]


def caixa(largura, altura, profundidade, cor):
    """Mesh em forma de caixa, centrada na origem local, com a cor indicada."""
    geometry = BoxGeometry(largura, altura, profundidade, faceColors=SOMBRA)
    material = BasicMaterial({'baseColor': cor, 'useVertexColors': True})
    return Mesh(geometry, material)
