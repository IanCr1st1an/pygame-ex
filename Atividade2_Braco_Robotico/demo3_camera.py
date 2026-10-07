# Demonstração 3: a câmera também é um Object3D.
#   W A S D: anda para frente/trás/lados (local)    Q E: vira à esquerda/direita
#   R F: sobe/desce    setas cima/baixo: inclina a câmera    ESC fecha. P salva uma captura.
import argparse

from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.object3D import Object3D
from formas import caixa


class Demo(Base):

    def initialize(self):
        self.renderer = Renderer(clearColor=[0.75, 0.85, 0.95])
        self.scene = Scene()

        # chão e uma "cidade" de caixas
        chao = caixa(14, 0.1, 14, [0.55, 0.6, 0.55])
        chao.setPosition([0, -0.05, 0])
        self.scene.add(chao)
        for i in range(-3, 4):
            for j in range(-3, 4):
                if (i + j) % 2 == 0:
                    altura = 0.4 + 0.3 * ((i * 7 + j * 3) % 5)
                    predio = caixa(0.8, altura, 0.8, [0.9, 0.55 + 0.05 * (i % 3), 0.35])
                    predio.setPosition([i * 1.6, altura / 2, j * 1.6])
                    self.scene.add(predio)

        # rig: o pivô gira na horizontal (Q E); a câmera, filha dele, inclina (setas)
        self.rig = Object3D()
        self.rig.setPosition([0, 3.0, 9])
        self.scene.add(self.rig)
        self.camera = Camera(aspectRatio=960 / 640)
        self.camera.rotateX(-0.3)
        self.rig.add(self.camera)

    def update(self):
        move = 3.0 * self.deltaTime
        turn = 1.5 * self.deltaTime
        if self.isKeyPressed('w'): self.rig.translate(0, 0, -move)
        if self.isKeyPressed('s'): self.rig.translate(0, 0, move)
        if self.isKeyPressed('a'): self.rig.translate(-move, 0, 0)
        if self.isKeyPressed('d'): self.rig.translate(move, 0, 0)
        if self.isKeyPressed('r'): self.rig.translate(0, move, 0)
        if self.isKeyPressed('f'): self.rig.translate(0, -move, 0)
        if self.isKeyPressed('q'): self.rig.rotateY(turn)
        if self.isKeyPressed('e'): self.rig.rotateY(-turn)
        if self.isKeyPressed('up'): self.camera.rotateX(turn)
        if self.isKeyPressed('down'): self.camera.rotateX(-turn)
        self.renderer.render(self.scene, self.camera)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--frames', type=int)
    parser.add_argument('--screenshot')
    args = parser.parse_args()
    Demo(title='Demo 3: câmera').run(args.frames, args.screenshot)
