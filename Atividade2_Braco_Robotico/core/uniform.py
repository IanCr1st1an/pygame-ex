import numpy as np
from OpenGL.GL import *


class Uniform:
    def __init__(self, dataType, data):
        self.dataType = dataType
        self.data = data
        self.variableRef = -1

    def locateVariable(self, programRef, variableName):
        self.variableRef = glGetUniformLocation(programRef, variableName)

    def uploadData(self):
        if self.variableRef < 0:
            return
        if self.dataType == 'mat4':
            # GLSL guarda por colunas: envia a transposta com transpose=GL_FALSE
            array = np.ascontiguousarray(np.asarray(self.data, dtype=np.float32).T)
            glUniformMatrix4fv(self.variableRef, 1, GL_FALSE, array)
        elif self.dataType in ('int', 'bool'):
            glUniform1i(self.variableRef, int(self.data))
        elif self.dataType == 'float':
            glUniform1f(self.variableRef, self.data)
        elif self.dataType == 'vec3':
            glUniform3fv(self.variableRef, 1, self.data)
        else:
            raise ValueError('Tipo de uniform não implementado: ' + self.dataType)
