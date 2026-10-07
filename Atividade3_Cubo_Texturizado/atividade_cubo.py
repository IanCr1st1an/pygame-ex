# Arquivo inicial da atividade. Leia ATIVIDADE.md e altere os trechos marcados com TODO.
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
IMAGENS=Path(__file__).resolve().parent/'images'
TEXTURA='mosaico.png'  # Requisito 1: textura do cubo principal
VELOCIDADE=0.8  # radianos por segundo
class Cubo(Base):
    def initialize(self):
        self.renderer=Renderer();self.scene=Scene()
        self.camera=Camera(aspectRatio=960/640)
        self.camera.setPosition([0,0,3.2])
        self.velocidade=VELOCIDADE
        # cubo principal
        textura=Texture(IMAGENS/TEXTURA)
        self.mesh=Mesh(BoxGeometry(),TextureMaterial(textura))
        self.mesh.rotateX(0.35);self.mesh.rotateY(0.5)
        self.scene.add(self.mesh)
        # Requisito 2: satélite = segundo cubo com grade_uv.png repetida 2x2 em cada face.
        # repeatUV multiplica as coordenadas UV no vertex shader (UV = vertexUV * repeatUV).
        texturaSatelite=Texture(IMAGENS/'grade_uv.png')
        self.satelite=Mesh(BoxGeometry(),TextureMaterial(texturaSatelite,{'repeatUV':[2,2]}))
        # Requisito 3: o satélite é FILHO do cubo principal, então herda a rotação dele (órbita).
        # Ordem: primeiro posiciona (setPosition define a translação, 1.3 no eixo X) e depois
        # escala (scale multiplica à direita: T @ S). Assim a escala 0.4 só encolhe o cubo e
        # não a distância até o centro, que continua 1.3.
        self.satelite.setPosition([1.3,0,0])
        self.satelite.scale(0.4)
        self.mesh.add(self.satelite)
    def update(self):
        # Requisito 4: setas 'up' e 'down' aumentam e diminuem self.velocidade.
        # A variação é de 1.0 rad/s por segundo de tecla pressionada (multiplicada por deltaTime,
        # para não depender da taxa de quadros). Abaixo de zero, o cubo passa a girar ao contrário.
        if self.isKeyPressed('up'): self.velocidade+=1.0*self.deltaTime
        if self.isKeyPressed('down'): self.velocidade-=1.0*self.deltaTime
        self.mesh.rotateY(self.velocidade*self.deltaTime)
        # Requisito 5: rotação própria do satélite em torno do SEU eixo X, a 2 rad/s.
        # rotateX é local (transform @ R), então gira no lugar, sem alterar a órbita.
        self.satelite.rotateX(2.0*self.deltaTime)
        self.renderer.render(self.scene,self.camera)
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--frames',type=int);parser.add_argument('--screenshot')
    args=parser.parse_args();Cubo().run(args.frames,args.screenshot)
