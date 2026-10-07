import os
os.environ.setdefault('PYGAME_HIDE_SUPPORT_PROMPT', '1')
from pathlib import Path

import pygame
from OpenGL.GL import *


class Base:
    """Janela, loop principal e teclado. Subclasses implementam initialize() e update()."""

    def __init__(self, screenSize=None, title='Grafo de cena com Python e OpenGL'):
        self.screenSize = screenSize or [960, 640]
        pygame.display.init()
        # contexto OpenGL 3.2 core (necessário no macOS)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 2)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_FLAGS, pygame.GL_CONTEXT_FORWARD_COMPATIBLE_FLAG)
        pygame.display.gl_set_attribute(pygame.GL_DEPTH_SIZE, 24)
        pygame.display.set_mode(self.screenSize, pygame.OPENGL | pygame.DOUBLEBUF)
        pygame.display.set_caption(title)
        glViewport(0, 0, *self.screenSize)
        self.clock = pygame.time.Clock()
        self.deltaTime = 0
        self.time = 0
        self.running = True
        self.keysDown = []

    def initialize(self):
        pass

    def update(self):
        pass

    def isKeyPressed(self, name):
        """True enquanto a tecla estiver pressionada. Nomes do pygame: 'a', 'up', 'space'..."""
        return pygame.key.get_pressed()[pygame.key.key_code(name)]

    def isKeyDown(self, name):
        """True apenas no quadro em que a tecla foi pressionada."""
        return name in self.keysDown

    def saveScreenshot(self, path):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        glReadBuffer(GL_BACK)
        w, h = self.screenSize
        data = glReadPixels(0, 0, w, h, GL_RGB, GL_UNSIGNED_BYTE)
        pygame.image.save(pygame.image.fromstring(data, (w, h), 'RGB', True), str(path))
        print('Captura salva em', path)

    def run(self, frames=None, screenshot=None):
        """frames/screenshot: opcionais, rodam N quadros e salvam a imagem final."""
        try:
            self.initialize()
            count = 0
            while self.running:
                self.deltaTime = self.clock.tick(60) / 1000
                self.time += self.deltaTime
                self.keysDown = []
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    if event.type == pygame.KEYDOWN:
                        self.keysDown.append(pygame.key.name(event.key))
                if self.isKeyDown('escape'):
                    self.running = False
                self.update()
                count += 1
                # tecla P salva uma captura para a entrega
                if self.isKeyDown('p'):
                    self.saveScreenshot('capturas/resultado.png')
                if frames is not None and count >= frames:
                    if screenshot:
                        self.saveScreenshot(screenshot)
                    self.running = False
                pygame.display.flip()
            error = glGetError()
            if error != GL_NO_ERROR:
                raise RuntimeError(f'OpenGL error: {error}')
        finally:
            pygame.quit()
