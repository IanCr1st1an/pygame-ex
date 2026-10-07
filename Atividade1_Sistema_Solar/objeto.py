from OpenGL.GL import *

from core.attribute import Attribute


class Objeto(object):
    """Guarda um VAO com posições e cores, pronto para ser desenhado.
    A matriz de modelo é enviada pelo programa principal antes do desenho."""

    def __init__(self, programRef, posicoes, cores, modo=GL_TRIANGLES):
        self.modo = modo
        self.vertexCount = len(posicoes)
        # cada objeto tem o seu próprio vertex array object
        self.vaoRef = glGenVertexArrays(1)
        glBindVertexArray(self.vaoRef)
        Attribute("vec3", posicoes).associateVariable(programRef, "position")
        Attribute("vec3", cores).associateVariable(programRef, "vertexColor")

    def desenhar(self):
        glBindVertexArray(self.vaoRef)
        glDrawArrays(self.modo, 0, self.vertexCount)
