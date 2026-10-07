import numpy as np

from core.object3D import Object3D
from core.matrix import Matrix


class Camera(Object3D):
    """A câmera é um Object3D: pode ser movida, girada e ter pai.
    viewMatrix é a inversa da matriz do mundo da câmera."""

    def __init__(self, angleOfView=60, aspectRatio=1, near=0.1, far=1000):
        super().__init__()
        self.projectionMatrix = Matrix.makePerspective(angleOfView, aspectRatio, near, far)
        self.viewMatrix = Matrix.makeIdentity()

    def updateViewMatrix(self):
        self.viewMatrix = np.linalg.inv(self.getWorldMatrix())
