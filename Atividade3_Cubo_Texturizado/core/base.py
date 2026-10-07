import os
os.environ.setdefault('PYGAME_HIDE_SUPPORT_PROMPT','1')
import pygame
from OpenGL.GL import *
class Base:
    def __init__(self,screenSize=None,title='Texturas com Python e OpenGL'):
        self.screenSize=screenSize or [960,640]
        pygame.display.init()
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION,3)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION,2)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK,pygame.GL_CONTEXT_PROFILE_CORE)
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_FLAGS,pygame.GL_CONTEXT_FORWARD_COMPATIBLE_FLAG)
        pygame.display.gl_set_attribute(pygame.GL_DEPTH_SIZE,24)
        pygame.display.set_mode(self.screenSize,pygame.OPENGL|pygame.DOUBLEBUF)
        pygame.display.set_caption(title);glViewport(0,0,*self.screenSize)
        self.clock=pygame.time.Clock();self.deltaTime=0;self.running=True
    def isKeyPressed(self,name):
        # True enquanto a tecla estiver pressionada. Nomes do pygame: 'up', 'down', 'a', 'space'...
        return pygame.key.get_pressed()[pygame.key.key_code(name)]
    def initialize(self): pass
    def update(self): pass
    def saveScreenshot(self,path):
        from pathlib import Path
        path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
        glReadBuffer(GL_BACK);w,h=self.screenSize
        data=glReadPixels(0,0,w,h,GL_RGB,GL_UNSIGNED_BYTE)
        surface=pygame.image.fromstring(data,(w,h),'RGB',True)
        pygame.image.save(surface,str(path))
    def run(self,frames=None,screenshot=None):
        try:
            self.initialize();number=0
            while self.running:
                self.deltaTime=self.clock.tick(60)/1000
                for event in pygame.event.get():
                    if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE): self.running=False
                    if event.type==pygame.KEYDOWN and event.key==pygame.K_s: self._capture=True
                self.update();number+=1
                if getattr(self,'_capture',False): self.saveScreenshot('capturas/resultado.png');self._capture=False
                if frames is not None and number>=frames:
                    if screenshot: self.saveScreenshot(screenshot)
                    self.running=False
                pygame.display.flip()
            error=glGetError()
            if error!=GL_NO_ERROR: raise RuntimeError(f'OpenGL error: {error}')
        finally: pygame.quit()
