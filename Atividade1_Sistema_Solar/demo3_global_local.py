# Demonstração 3: transformações globais x locais e projeção.
#   Global (multiplica à ESQUERDA):  W A S D movem, Z X aproximam/afastam, Q E giram em torno da origem
#   Local  (multiplica à DIREITA):   I J K L movem na direção da seta, U O giram em torno do próprio centro
#   V alterna perspectiva/ortográfica   R reinicia   P salva captura   ESC fecha
import argparse
from math import pi, tan, radians

import pygame
from OpenGL.GL import *

from core.base import Base
from core.utils import Utils
from core.uniform import Uniform
from core.matrix import Matrix
from formas import seta, eixos
from objeto import Objeto
from shaders import VERTEX_SHADER, FRAGMENT_SHADER

# metade da altura visível a 1 unidade da câmera, para as duas projeções coincidirem em z = -1
METADE = tan(radians(60) / 2)


class Demo(Base):

    def initialize(self):
        self.programRef = Utils.initialize_program(VERTEX_SHADER, FRAGMENT_SHADER)
        glClearColor(0.09, 0.12, 0.17, 1.0)
        glEnable(GL_DEPTH_TEST)
        # LEQUAL: a seta vence os eixos quando estão na mesma profundidade
        glDepthFunc(GL_LEQUAL)

        self.eixos = Objeto(self.programRef, *eixos(), modo=GL_LINES)
        self.seta = Objeto(self.programRef, *seta())

        # a seta começa 1 unidade à frente da câmera (a câmera olha para -z)
        self.modelMatrix = Uniform("mat4", Matrix.make_translation(0, 0, -1))
        self.modelMatrix.locateVariable(self.programRef, "modelMatrix")
        # os eixos ficam fixos no mesmo plano z = -1
        self.eixosMatrix = Matrix.make_translation(0, 0, -1)

        self.perspectiva = True
        self.projectionMatrix = Uniform("mat4", Matrix.make_perspective())
        self.projectionMatrix.locateVariable(self.programRef, "projectionMatrix")

        # velocidades: unidades por segundo e radianos por segundo
        self.moveSpeed = 0.5
        self.turnSpeed = 90 * (pi / 180)

    def trocarProjecao(self):
        self.perspectiva = not self.perspectiva
        if self.perspectiva:
            self.projectionMatrix.data = Matrix.make_perspective()
            nome = "perspectiva"
        else:
            self.projectionMatrix.data = Matrix.make_orthographic(
                -METADE, METADE, -METADE, METADE, 0.1, 1000)
            nome = "ortográfica"
        pygame.display.set_caption("Demo 3: projeção " + nome)
        print("Projeção", nome)

    def update(self):
        move = self.moveSpeed * self.deltaTime
        turn = self.turnSpeed * self.deltaTime

        # tecla -> matriz; GLOBAL multiplica à esquerda
        globais = {
            "w": Matrix.make_translation(0, move, 0),
            "s": Matrix.make_translation(0, -move, 0),
            "a": Matrix.make_translation(-move, 0, 0),
            "d": Matrix.make_translation(move, 0, 0),
            "z": Matrix.make_translation(0, 0, move),
            "x": Matrix.make_translation(0, 0, -move),
            "q": Matrix.make_rotation_z(turn),
            "e": Matrix.make_rotation_z(-turn),
        }
        # LOCAL multiplica à direita
        locais = {
            "i": Matrix.make_translation(0, move, 0),
            "k": Matrix.make_translation(0, -move, 0),
            "j": Matrix.make_translation(-move, 0, 0),
            "l": Matrix.make_translation(move, 0, 0),
            "u": Matrix.make_rotation_z(turn),
            "o": Matrix.make_rotation_z(-turn),
        }
        for tecla, m in globais.items():
            if self.input.isKeyPressed(tecla):
                self.modelMatrix.data = m @ self.modelMatrix.data
        for tecla, m in locais.items():
            if self.input.isKeyPressed(tecla):
                self.modelMatrix.data = self.modelMatrix.data @ m

        if self.input.isKeyDown("v"):
            self.trocarProjecao()
        if self.input.isKeyDown("r"):
            self.modelMatrix.data = Matrix.make_translation(0, 0, -1)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glUseProgram(self.programRef)
        self.projectionMatrix.uploadData()

        # guarda a matriz da seta, desenha os eixos e depois a seta
        matrizSeta = self.modelMatrix.data
        self.modelMatrix.data = self.eixosMatrix
        self.modelMatrix.uploadData()
        self.eixos.desenhar()

        self.modelMatrix.data = matrizSeta
        self.modelMatrix.uploadData()
        self.seta.desenhar()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--frames", type=int)
    parser.add_argument("--screenshot")
    args = parser.parse_args()
    Demo(title="Demo 3: global x local").run(args.frames, args.screenshot)
