import os
os.environ.setdefault('PYGAME_HIDE_SUPPORT_PROMPT', '1')

from pathlib import Path

import pygame
from OpenGL.GL import *

from core.input import Input


class Base(object):
    def __init__(self, screenSize=[640, 640], title="Transformações com Python e OpenGL"):

        # inicializa todos os módulos do pygame
        pygame.init()
        self.screenSize = screenSize
        # indica os detalhes de renderização
        displayFlags = pygame.DOUBLEBUF | pygame.OPENGL
        # inicializa buffers para realizar antialiasing
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
        # pede explicitamente OpenGL 3.3 core (necessário no macOS para usar #version 330)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)
        pygame.display.gl_set_attribute(
            pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
        pygame.display.gl_set_attribute(
            pygame.GL_CONTEXT_FLAGS, pygame.GL_CONTEXT_FORWARD_COMPATIBLE_FLAG)
        # buffer de profundidade, usado com GL_DEPTH_TEST
        pygame.display.gl_set_attribute(pygame.GL_DEPTH_SIZE, 24)
        # cria e mostra a janela
        self.screen = pygame.display.set_mode(screenSize, displayFlags)
        # define o texto que aparece na barra de título da janela
        pygame.display.set_caption(title)

        # determina se o loop principal está ativo
        self.running = True
        # gere dados e operações relacionadas com o tempo
        self.clock = pygame.time.Clock()
        # gere a entrada do utilizador
        self.input = Input()
        # número de segundos que a aplicação está em execução
        self.time = 0
        # segundos desde a última iteração do loop principal
        self.deltaTime = 0

    # implementar através de extensão da classe
    def initialize(self):
        pass

    # implementar através de extensão da classe
    def update(self):
        pass

    # salva o conteúdo da janela em um arquivo PNG
    def saveScreenshot(self, path):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        glReadBuffer(GL_BACK)
        width, height = self.screenSize
        data = glReadPixels(0, 0, width, height, GL_RGB, GL_UNSIGNED_BYTE)
        surface = pygame.image.fromstring(data, (width, height), 'RGB', True)
        pygame.image.save(surface, str(path))
        print('Captura salva em', path)

    # frames e screenshot são opcionais: permitem rodar N quadros e salvar a imagem final
    def run(self, frames=None, screenshot=None):
        ## arranque ##
        self.initialize()
        frameCount = 0

        ## loop principal ##
        while self.running:
            ## processa entrada ##
            self.input.update()
            if self.input.quit or self.input.isKeyDown('escape'):
                self.running = False

            # segundos desde a última iteração do loop principal
            self.deltaTime = self.clock.get_time() / 1000
            # incrementa o tempo que a aplicação está em execução
            self.time += self.deltaTime

            ## atualização ##
            self.update()
            frameCount += 1

            # tecla P salva uma captura (para a entrega da atividade)
            if self.input.isKeyDown('p'):
                self.saveScreenshot('capturas/resultado.png')
            if frames is not None and frameCount >= frames:
                if screenshot:
                    self.saveScreenshot(screenshot)
                self.running = False

            ## renderização ##
            # mostra a imagem no ecrã
            pygame.display.flip()

            # pausa se necessário para atingir 60 FPS
            self.clock.tick(60)

        ## encerramento ##
        pygame.quit()
