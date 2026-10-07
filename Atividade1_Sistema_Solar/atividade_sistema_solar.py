# ATIVIDADE: mini sistema solar com composição de matrizes.
# Leia ATIVIDADE.md. Altere apenas os trechos marcados com TODO.
# ESC fecha. P salva capturas/resultado.png para a entrega.
import argparse

from OpenGL.GL import *

from core.base import Base
from core.utils import Utils
from core.uniform import Uniform
from core.matrix import Matrix
from formas import quadrado
from objeto import Objeto
from shaders import VERTEX_SHADER, FRAGMENT_SHADER

RAIO_ORBITA_PLANETA = 0.6
RAIO_ORBITA_LUA = 0.2


class SistemaSolar(Base):

    def initialize(self):
        self.programRef = Utils.initialize_program(VERTEX_SHADER, FRAGMENT_SHADER)
        glClearColor(0.04, 0.05, 0.10, 1.0)

        # quadrados de lado 2, centrados na origem (coordenadas locais)
        self.sol = Objeto(self.programRef, *quadrado([1.0, 0.75, 0.1], [1.0, 0.5, 0.0]))
        self.planeta = Objeto(self.programRef, *quadrado([0.2, 0.5, 1.0], [0.1, 0.3, 0.7]))
        self.lua = Objeto(self.programRef, *quadrado([0.85, 0.85, 0.85], [0.5, 0.5, 0.5]))

        self.modelMatrix = Uniform("mat4", Matrix.make_identity())
        self.modelMatrix.locateVariable(self.programRef, "modelMatrix")
        self.projectionMatrix = Uniform("mat4", Matrix.make_orthographic())
        self.projectionMatrix.locateVariable(self.programRef, "projectionMatrix")

        # velocidades em radianos por segundo
        self.velocidadeSol = 0.3
        self.velocidadeOrbita = 0.8
        self.velocidadeRotacaoPlaneta = 3.0
        self.velocidadeOrbitaLua = 2.5

        # ângulos acumulados: somar velocidade * deltaTime evita "saltos"
        # quando a velocidade muda durante a execução
        self.anguloSol = 0.0
        self.anguloOrbita = 0.0
        self.anguloRotacaoPlaneta = 0.0
        self.anguloOrbitaLua = 0.0

    def update(self):
        # Requisito 5: setas para cima/baixo ("up"/"down") alteram self.velocidadeOrbita.
        # A variação é por segundo (1.0 rad/s a cada segundo com a tecla pressionada),
        # então não depende da taxa de quadros. max(0, ...) impede velocidade negativa.
        if self.input.isKeyPressed("up"):
            self.velocidadeOrbita += 1.0 * self.deltaTime
        if self.input.isKeyPressed("down"):
            self.velocidadeOrbita -= 1.0 * self.deltaTime
        self.velocidadeOrbita = max(0.0, self.velocidadeOrbita)

        self.anguloSol += self.velocidadeSol * self.deltaTime
        self.anguloOrbita += self.velocidadeOrbita * self.deltaTime
        self.anguloRotacaoPlaneta += self.velocidadeRotacaoPlaneta * self.deltaTime
        self.anguloOrbitaLua += self.velocidadeOrbitaLua * self.deltaTime

        # Requisito 1: o sol gira em torno do próprio centro.
        # Lido da direita para a esquerda: escala -> rotação (no centro, pois ainda está na origem).
        matrizSol = Matrix.make_rotation_z(self.anguloSol) @ Matrix.make_scale(0.25)

        # Requisito 2: a órbita do planeta é R(órbita) @ T(raio). Primeiro afasta o objeto
        # do sol (T) e depois gira todo o conjunto em torno da origem (R). Essa matriz é
        # guardada à parte porque a lua vai reaproveitá-la (requisito 4).
        orbitaPlaneta = Matrix.make_rotation_z(self.anguloOrbita) @ Matrix.make_translation(RAIO_ORBITA_PLANETA, 0, 0)
        # Requisito 3: a rotação própria fica À DIREITA da translação, ou seja, é aplicada
        # antes dela, com o planeta ainda na origem. Ordem: escala -> rotação própria -> órbita.
        matrizPlaneta = orbitaPlaneta @ Matrix.make_rotation_z(self.anguloRotacaoPlaneta) @ Matrix.make_scale(0.1)

        # Requisito 4: a lua parte da matriz da órbita do planeta (acompanha o planeta ao redor
        # do sol, mas sem herdar a rotação própria dele) e então faz a sua própria órbita
        # R(órbita da lua) @ T(raio da lua). A escala continua à direita de tudo.
        matrizLua = (orbitaPlaneta
                     @ Matrix.make_rotation_z(self.anguloOrbitaLua)
                     @ Matrix.make_translation(RAIO_ORBITA_LUA, 0, 0)
                     @ Matrix.make_scale(0.05))

        glClear(GL_COLOR_BUFFER_BIT)
        glUseProgram(self.programRef)
        self.projectionMatrix.uploadData()
        for objeto, matriz in [(self.sol, matrizSol),
                               (self.planeta, matrizPlaneta),
                               (self.lua, matrizLua)]:
            self.modelMatrix.data = matriz
            self.modelMatrix.uploadData()
            objeto.desenhar()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--frames", type=int)
    parser.add_argument("--screenshot")
    args = parser.parse_args()
    SistemaSolar(title="Atividade: sistema solar").run(args.frames, args.screenshot)
