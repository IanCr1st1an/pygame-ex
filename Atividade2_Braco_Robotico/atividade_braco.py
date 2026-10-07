# ATIVIDADE: braço robótico com grafo de cena.
# Leia ATIVIDADE.md e complete os trechos marcados com TODO.
# ESC fecha. P salva capturas/resultado.png para a entrega.
import argparse

from core.base import Base
from core.renderer import Renderer
from core.scene import Scene
from core.camera import Camera
from core.object3D import Object3D
from formas import caixa

CINZA = [0.6, 0.62, 0.66]
LARANJA = [0.98, 0.45, 0.2]
AZUL = [0.25, 0.5, 0.95]
VELOCIDADE = 1.5  # radianos por segundo


class Braco(Base):

    def initialize(self):
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspectRatio=960 / 640)
        self.camera.setPosition([0, 1.9, 4.2])
        self.camera.rotateX(-0.2)

        chao = caixa(6, 0.1, 6, [0.8, 0.82, 0.85])
        chao.setPosition([0, -0.05, 0])
        self.scene.add(chao)

        # base: caixa de altura 0.4, apoiada no chão
        self.base = caixa(1.0, 0.4, 1.0, CINZA)
        self.base.setPosition([0, 0.2, 0])
        self.scene.add(self.base)

        # Requisito 1: ombro (pivô) no TOPO da base. A base tem altura 0.4 e é centrada na
        # origem dela, então o topo fica em y = +0.2 (coordenadas locais da base).
        self.ombro = Object3D()
        self.ombro.setPosition([0, 0.2, 0])
        self.base.add(self.ombro)
        # O braço (altura 1.2) é centrado no próprio centro; subindo metade da altura (0.6),
        # a ponta de BAIXO coincide com o pivô do ombro.
        self.braco = caixa(0.3, 1.2, 0.3, LARANJA)
        self.braco.setPosition([0, 0.6, 0])
        self.ombro.add(self.braco)

        # Requisito 2: cotovelo (pivô) na ponta de CIMA do braço: y = 1.2 no sistema do ombro.
        # Ele é filho do OMBRO (e não do braço), para acompanhar o ombro mas ter giro próprio.
        self.cotovelo = Object3D()
        self.cotovelo.setPosition([0, 1.2, 0])
        self.ombro.add(self.cotovelo)
        # O antebraço (altura 1.0) sobe 0.5 para que a ponta de BAIXO fique no cotovelo.
        self.antebraco = caixa(0.25, 1.0, 0.25, AZUL)
        self.antebraco.setPosition([0, 0.5, 0])
        self.cotovelo.add(self.antebraco)

        # Requisito 3: garra (altura 0.15) na ponta de CIMA do antebraço, filha dele.
        # Topo do antebraço = y 0.5; o centro da garra fica 0.15 / 2 = 0.075 acima disso.
        self.garra = caixa(0.5, 0.15, 0.5, CINZA)
        self.garra.setPosition([0, 0.5 + 0.075, 0])
        self.antebraco.add(self.garra)

    def update(self):
        angulo = VELOCIDADE * self.deltaTime
        # Requisito 4: A e D giram a base em torno do eixo Y. Como o ombro (e tudo abaixo
        # dele) é descendente da base, o braço inteiro gira junto.
        if self.isKeyPressed('a'):
            self.base.rotateY(angulo)
        if self.isKeyPressed('d'):
            self.base.rotateY(-angulo)
        # Requisito 5: W e S giram o ombro; I e K giram o cotovelo, ambos em torno do eixo Z.
        # Girar o pivô leva junto tudo que é filho dele (antebraço e garra, no caso do ombro).
        if self.isKeyPressed('w'):
            self.ombro.rotateZ(angulo)
        if self.isKeyPressed('s'):
            self.ombro.rotateZ(-angulo)
        if self.isKeyPressed('i'):
            self.cotovelo.rotateZ(angulo)
        if self.isKeyPressed('k'):
            self.cotovelo.rotateZ(-angulo)
        self.renderer.render(self.scene, self.camera)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--frames', type=int)
    parser.add_argument('--screenshot')
    args = parser.parse_args()
    Braco(title='Atividade: braço robótico').run(args.frames, args.screenshot)
