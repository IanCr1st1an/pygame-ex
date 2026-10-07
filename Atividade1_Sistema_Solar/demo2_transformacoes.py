# Demonstração 2: translação, rotação, escala e a ordem da composição.
# Teclas 1 a 6 escolhem a transformação. ESC fecha. P salva uma captura.
import argparse
from math import sin

import pygame
from OpenGL.GL import *

from core.base import Base
from core.utils import Utils
from core.uniform import Uniform
from core.matrix import Matrix
from formas import seta, eixos
from objeto import Objeto
from shaders import VERTEX_SHADER, FRAGMENT_SHADER

MODOS = {
    "1": "Identidade",
    "2": "Translação T",
    "3": "Rotação R",
    "4": "Escala S",
    "5": "T @ R (gira e depois translada)",
    "6": "R @ T (translada e depois gira)",
}


class Demo(Base):

    def __init__(self, modo="1"):
        super().__init__(title="Demo 2: transformações")
        self.modo = modo

    def initialize(self):
        self.programRef = Utils.initialize_program(VERTEX_SHADER, FRAGMENT_SHADER)
        glClearColor(0.09, 0.12, 0.17, 1.0)

        self.eixos = Objeto(self.programRef, *eixos(), modo=GL_LINES)
        # cópia cinza: mostra a posição original da seta
        self.original = Objeto(self.programRef, *seta([0.35, 0.38, 0.42], [0.45, 0.48, 0.52]))
        self.seta = Objeto(self.programRef, *seta())

        self.modelMatrix = Uniform("mat4", Matrix.make_identity())
        self.modelMatrix.locateVariable(self.programRef, "modelMatrix")
        # projeção ortográfica: mantém as coordenadas de -1 a 1
        self.projectionMatrix = Uniform("mat4", Matrix.make_orthographic())
        self.projectionMatrix.locateVariable(self.programRef, "projectionMatrix")

        self.atualizarTitulo()

    def atualizarTitulo(self):
        pygame.display.set_caption("Modo " + self.modo + ": " + MODOS[self.modo])
        print("Modo", self.modo, "-", MODOS[self.modo])

    def update(self):
        for tecla in MODOS:
            if self.input.isKeyDown(tecla):
                self.modo = tecla
                self.atualizarTitulo()

        # valores animados com o tempo
        deslocamento = 0.5
        angulo = self.time
        escala = 1.5 + 0.5 * sin(2 * self.time)

        T = Matrix.make_translation(deslocamento, 0, 0)
        R = Matrix.make_rotation_z(angulo)
        S = Matrix.make_scale(escala)
        matrizes = {
            "1": Matrix.make_identity(),
            "2": T,
            "3": R,
            "4": S,
            "5": T @ R,
            "6": R @ T,
        }

        glClear(GL_COLOR_BUFFER_BIT)
        glUseProgram(self.programRef)
        self.projectionMatrix.uploadData()

        self.modelMatrix.data = Matrix.make_identity()
        self.modelMatrix.uploadData()
        self.eixos.desenhar()
        self.original.desenhar()

        self.modelMatrix.data = matrizes[self.modo]
        self.modelMatrix.uploadData()
        self.seta.desenhar()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--modo", default="1", choices=list(MODOS))
    parser.add_argument("--frames", type=int)
    parser.add_argument("--screenshot")
    args = parser.parse_args()
    Demo(args.modo).run(args.frames, args.screenshot)
