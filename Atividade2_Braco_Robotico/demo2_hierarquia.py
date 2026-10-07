# Demonstração 2: sistema solar com hierarquia (o mesmo da aula de Transformações,
# agora sem multiplicar matrizes à mão). ESPAÇO pausa. ESC fecha. P salva uma captura.
import argparse

from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.object3D import Object3D
from formas import caixa


class Demo(Base):

    def initialize(self):
        self.renderer = Renderer(clearColor=[0.05, 0.06, 0.12])
        self.scene = Scene()
        self.camera = Camera(aspectRatio=960 / 640)
        self.camera.setPosition([0, 2.6, 5])
        self.camera.rotateX(-0.45)

        self.sol = caixa(1.2, 1.2, 1.2, [1.0, 0.75, 0.2])
        self.scene.add(self.sol)

        # pivô invisível: girar a órbita leva o planeta junto
        self.orbitaPlaneta = Object3D()
        self.scene.add(self.orbitaPlaneta)
        self.planeta = caixa(0.5, 0.5, 0.5, [0.3, 0.6, 1.0])
        self.planeta.setPosition([2.6, 0, 0])
        self.orbitaPlaneta.add(self.planeta)

        # a órbita da lua fica na posição do planeta, mas não herda a rotação própria dele
        self.orbitaLua = Object3D()
        self.orbitaLua.setPosition([2.6, 0, 0])
        self.orbitaPlaneta.add(self.orbitaLua)
        self.lua = caixa(0.2, 0.2, 0.2, [0.85, 0.85, 0.85])
        self.lua.setPosition([0.7, 0, 0])
        self.orbitaLua.add(self.lua)

        self.pausado = False

    def update(self):
        if self.isKeyDown('space'):
            self.pausado = not self.pausado
        if not self.pausado:
            dt = self.deltaTime
            self.sol.rotateY(0.3 * dt)
            self.orbitaPlaneta.rotateY(0.6 * dt)
            self.planeta.rotateY(2.5 * dt)
            self.orbitaLua.rotateY(2.0 * dt)
        self.renderer.render(self.scene, self.camera)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--frames', type=int)
    parser.add_argument('--screenshot')
    args = parser.parse_args()
    Demo(title='Demo 2: hierarquia').run(args.frames, args.screenshot)
