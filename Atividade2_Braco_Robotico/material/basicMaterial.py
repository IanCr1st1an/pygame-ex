from material.material import Material

VERTEX_SHADER = """#version 150 core
uniform mat4 projectionMatrix;
uniform mat4 viewMatrix;
uniform mat4 modelMatrix;
in vec3 vertexPosition;
in vec3 vertexColor;
out vec3 color;
void main() {
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(vertexPosition, 1.0);
    color = vertexColor;
}
"""

FRAGMENT_SHADER = """#version 150 core
uniform vec3 baseColor;
uniform bool useVertexColors;
in vec3 color;
out vec4 fragColor;
void main() {
    vec3 c = baseColor;
    if (useVertexColors) c *= color;
    fragColor = vec4(c, 1.0);
}
"""


class BasicMaterial(Material):
    """Cor única (baseColor) ou cores por vértice multiplicadas por baseColor."""

    def __init__(self, properties=None):
        super().__init__(VERTEX_SHADER, FRAGMENT_SHADER)
        self.addUniform('vec3', 'baseColor', [1.0, 1.0, 1.0])
        self.addUniform('bool', 'useVertexColors', False)
        self.setProperties(properties or {})
        self.locateUniforms()
