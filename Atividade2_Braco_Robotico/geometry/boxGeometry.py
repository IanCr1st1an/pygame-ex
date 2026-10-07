from geometry.geometry import Geometry


class BoxGeometry(Geometry):
    """Caixa centrada na origem: 6 faces x 2 triângulos = 36 vértices.
    Cada face recebe uma cor (vertexColor), para a rotação ficar visível.
    faceColors: lista opcional com 6 cores, na ordem +x, -x, +y, -y, +z, -z."""

    def __init__(self, width=1, height=1, depth=1, faceColors=None):
        super().__init__()
        w, h, d = width / 2, height / 2, depth / 2
        P0, P1, P2, P3 = [-w, -h, -d], [w, -h, -d], [-w, h, -d], [w, h, -d]
        P4, P5, P6, P7 = [-w, -h, d], [w, -h, d], [-w, h, d], [w, h, d]
        positionData = [P5, P1, P3, P5, P3, P7,   # +x
                        P0, P4, P6, P0, P6, P2,   # -x
                        P6, P7, P3, P6, P3, P2,   # +y
                        P0, P1, P5, P0, P5, P4,   # -y
                        P4, P5, P7, P4, P7, P6,   # +z
                        P1, P0, P2, P1, P2, P3]   # -z
        # tons claros e escuros por eixo: x vermelho, y verde, z azul
        faceColors = faceColors or [[1.0, 0.5, 0.5], [0.5, 0.0, 0.0],
                                    [0.5, 1.0, 0.5], [0.0, 0.5, 0.0],
                                    [0.5, 0.5, 1.0], [0.0, 0.0, 0.5]]
        colorData = [c for c in faceColors for _ in range(6)]
        self.addAttribute('vec3', 'vertexPosition', positionData)
        self.addAttribute('vec3', 'vertexColor', colorData)
        self.countVertices()
