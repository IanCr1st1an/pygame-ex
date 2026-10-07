from pathlib import Path
import argparse
from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from core.texture import Texture
from material.textureMaterial import TextureMaterial

from geometry.boxGeometry import BoxGeometry
TEXTURA='grade_uv.png'
VELOCIDADE=0.8  # radianos por segundo
EIXO='Y'
class Cubo(Base):
    def initialize(self):
        self.renderer=Renderer();self.scene=Scene()
        self.camera=Camera(aspectRatio=960/640)
        self.camera.setPosition([0,0,3.2])
        geometry=BoxGeometry()
        grid=Texture(Path(__file__).resolve().parent/'images'/TEXTURA)
        material=TextureMaterial(grid)
        self.mesh=Mesh(geometry,material)
        self.mesh.rotateX(0.35);self.mesh.rotateY(0.5)
        self.scene.add(self.mesh)
    def update(self):
        angle=VELOCIDADE*self.deltaTime
        if EIXO=='X': self.mesh.rotateX(angle)
        elif EIXO=='Y': self.mesh.rotateY(angle)
        elif EIXO=='Z': self.mesh.rotateZ(angle)
        else: raise ValueError('EIXO deve ser X, Y ou Z')
        self.renderer.render(self.scene,self.camera)
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--frames',type=int);parser.add_argument('--screenshot')
    args=parser.parse_args();Cubo().run(args.frames,args.screenshot)
