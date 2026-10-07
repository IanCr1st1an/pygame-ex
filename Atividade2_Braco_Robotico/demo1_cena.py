# Demonstração 1: a "receita" de uma cena - Renderer, Scene, Camera e Mesh.
# ESC fecha. P salva uma captura.
import argparse

from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from geometry.boxGeometry import BoxGeometry
from material.basicMaterial import BasicMaterial


class Demo(Base):

    def initialize(self):
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=960 / 640)
        self.camera.setPosition([0, 0, 3])

        geometry = BoxGeometry()                                  # vértices
        material = BasicMaterial({'useVertexColors': True})       # shaders
        self.mesh = Mesh(geometry, material)                      # objeto visível
        self.scene.add(self.mesh)

    def update(self):
        # rotações locais (no próprio centro), em radianos por segundo
        self.mesh.rotateY(0.9 * self.deltaTime)
        self.mesh.rotateX(0.6 * self.deltaTime)
        self.renderer.render(self.scene, self.camera)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--frames', type=int)
    parser.add_argument('--screenshot')
    args = parser.parse_args()
    Demo(title='Demo 1: cena básica').run(args.frames, args.screenshot)
