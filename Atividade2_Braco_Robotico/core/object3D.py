from core.matrix import Matrix


class Object3D:
    """Nó do grafo de cena: uma matriz local (transform), um pai e uma lista de filhos."""

    def __init__(self):
        self.transform = Matrix.makeIdentity()
        self.parent = None
        self.children = []

    def add(self, child):
        self.children.append(child)
        child.parent = self

    def remove(self, child):
        self.children.remove(child)
        child.parent = None

    def getWorldMatrix(self):
        """Matriz do mundo = matriz do mundo do pai @ matriz local."""
        if self.parent is None:
            return self.transform
        return self.parent.getWorldMatrix() @ self.transform

    def getDescendantList(self):
        """Este nó e todos os descendentes (usado pelo Renderer)."""
        result = [self]
        for child in self.children:
            result.extend(child.getDescendantList())
        return result

    # localCoord=True: multiplica à direita (eixos do objeto)
    # localCoord=False: multiplica à esquerda (eixos do pai)
    def applyMatrix(self, matrix, localCoord=True):
        if localCoord:
            self.transform = self.transform @ matrix
        else:
            self.transform = matrix @ self.transform

    def translate(self, x, y, z, localCoord=True):
        self.applyMatrix(Matrix.makeTranslation(x, y, z), localCoord)

    def rotateX(self, angle, localCoord=True):
        self.applyMatrix(Matrix.makeRotationX(angle), localCoord)

    def rotateY(self, angle, localCoord=True):
        self.applyMatrix(Matrix.makeRotationY(angle), localCoord)

    def rotateZ(self, angle, localCoord=True):
        self.applyMatrix(Matrix.makeRotationZ(angle), localCoord)

    def scale(self, s, localCoord=True):
        self.applyMatrix(Matrix.makeScale(s), localCoord)

    def setPosition(self, position):
        self.transform[:3, 3] = position

    def getPosition(self):
        return self.transform[:3, 3].tolist()

    def getWorldPosition(self):
        return self.getWorldMatrix()[:3, 3].tolist()
