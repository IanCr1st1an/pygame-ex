from OpenGL.GL import *
import numpy


class Attribute(object):

    def __init__(self, dataType, data):

        # tipo dos elementos no array de dados
        #   int | float | vec2 | vec3 | vec4
        self.dataType = dataType

        # array de dados a ser armazenado no buffer
        self.data = data

        # referência para o buffer disponível na GPU
        self.bufferRef = glGenBuffers(1)

        # envia os dados imediatamente
        self.uploadData()

    # envia estes dados para um buffer da GPU

    def uploadData(self):

        # converte os dados para o formato de array numpy;
        #    converte os números para floats de 32 bits
        data = numpy.array(self.data).astype(numpy.float32)

        # seleciona o buffer usado pelas funções seguintes
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)

        # armazena os dados no buffer atualmente associado
        glBufferData(GL_ARRAY_BUFFER, data.ravel(), GL_STATIC_DRAW)

    # associa uma variável do programa a este buffer

    def associateVariable(self, programRef, variableName):

        # obtém a referência da variável do programa com o nome indicado
        variableRef = glGetAttribLocation(programRef, variableName)

        # se o programa não referenciar a variável, sai
        if variableRef == -1:
            return

        # seleciona o buffer usado pelas funções seguintes
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)

        # especifica como os dados serão lidos
        #   do buffer atualmente associado para a variável
        # especificada
        if self.dataType == "int":
            glVertexAttribPointer(variableRef, 1, GL_INT, False, 0, None)
        elif self.dataType == "float":
            glVertexAttribPointer(variableRef, 1, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec2":
            glVertexAttribPointer(variableRef, 2, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec3":
            glVertexAttribPointer(variableRef, 3, GL_FLOAT, False, 0, None)
        elif self.dataType == "vec4":
            glVertexAttribPointer(variableRef, 4, GL_FLOAT, False, 0, None)
        else:
            raise Exception("Attribution " + variableName +
                            " has unkown type " + self.dataType)

        # indica que os dados serão transmitidos para esta variável
        glEnableVertexAttribArray(variableRef)
