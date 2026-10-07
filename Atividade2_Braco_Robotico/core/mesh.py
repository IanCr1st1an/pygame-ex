from OpenGL.GL import *

from core.object3D import Object3D


class Mesh(Object3D):
    """Objeto visível: junta uma Geometry (vértices) e um Material (shaders)."""

    def __init__(self, geometry, material):
        super().__init__()
        self.geometry = geometry
        self.material = material
        self.visible = True
        # o VAO guarda a ligação entre os atributos da geometria e o programa do material
        self.vaoRef = glGenVertexArrays(1)
        glBindVertexArray(self.vaoRef)
        for name, attribute in geometry.attributes.items():
            attribute.associateVariable(material.programRef, name)
        glBindVertexArray(0)
