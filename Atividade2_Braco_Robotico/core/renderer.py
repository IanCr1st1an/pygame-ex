from OpenGL.GL import *

from core.mesh import Mesh


class Renderer:
    def __init__(self, clearColor=None):
        clearColor = clearColor or [0.94, 0.95, 0.97]
        glEnable(GL_DEPTH_TEST)
        glClearColor(*clearColor, 1)

    def render(self, scene, camera):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        camera.updateViewMatrix()
        # percorre a árvore e desenha cada Mesh
        for mesh in scene.getDescendantList():
            if not isinstance(mesh, Mesh) or not mesh.visible:
                continue
            material = mesh.material
            glUseProgram(material.programRef)
            glBindVertexArray(mesh.vaoRef)
            material.uniforms['modelMatrix'].data = mesh.getWorldMatrix()
            material.uniforms['viewMatrix'].data = camera.viewMatrix
            material.uniforms['projectionMatrix'].data = camera.projectionMatrix
            for uniform in material.uniforms.values():
                uniform.uploadData()
            material.updateRenderSettings()
            glDrawArrays(material.settings['drawStyle'], 0, mesh.geometry.vertexCount)
        glBindVertexArray(0)
