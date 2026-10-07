from pathlib import Path
import argparse
from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.mesh import Mesh
from core.texture import Texture
from material.textureMaterial import TextureMaterial

from geometry.rectangleGeometry import RectangleGeometry
REPETICAO=1  # quantas vezes a imagem se repete em U e em V (repeatUV)
class Retangulo(Base):
    def initialize(self):
        self.renderer=Renderer();self.scene=Scene()
        self.camera=Camera(aspectRatio=960/640)
        self.camera.setPosition([0,0,2.5])
        geometry=RectangleGeometry(width=2,height=2)
        grid=Texture(Path(__file__).resolve().parent/'images'/'grade_uv.png')
        material=TextureMaterial(grid,{'repeatUV':[REPETICAO,REPETICAO]})
        self.mesh=Mesh(geometry,material);self.scene.add(self.mesh)
    def update(self): self.renderer.render(self.scene,self.camera)
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--frames',type=int);parser.add_argument('--screenshot')
    parser.add_argument('--repetir',type=float,help='valor de repeatUV, por exemplo 2')
    args=parser.parse_args()
    if args.repetir is not None: REPETICAO=args.repetir
    Retangulo().run(args.frames,args.screenshot)
