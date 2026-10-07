from pathlib import Path
from OpenGL.GL import *
from material.material import Material
class TextureMaterial(Material):
    def __init__(self,texture,properties=None):
        shaderDir=Path(__file__).resolve().parents[1]/'shaders'
        super().__init__((shaderDir/'texture.vert').read_text(),(shaderDir/'texture.frag').read_text())
        self.addUniform('vec3','baseColor',[1.0,1.0,1.0])
        self.addUniform('sampler2D','textureSampler',[texture.textureRef,1])
        self.addUniform('vec2','repeatUV',[1.0,1.0])
        self.addUniform('vec2','offsetUV',[0.0,0.0])
        self.settings.update(doubleSide=True,wireframe=False,lineWidth=1)
        self.setProperties(properties or {});self.locateUniforms()
    def updateRenderSettings(self):
        if self.settings['doubleSide']: glDisable(GL_CULL_FACE)
        else: glEnable(GL_CULL_FACE)
        glPolygonMode(GL_FRONT_AND_BACK,GL_LINE if self.settings['wireframe'] else GL_FILL)
        glLineWidth(self.settings['lineWidth'])
