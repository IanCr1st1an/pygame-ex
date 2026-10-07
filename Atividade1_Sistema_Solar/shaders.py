# Shaders usados por todos os exemplos da aula.
# A posição final é: projeção * modelo * posição local.

VERTEX_SHADER = """
in vec3 position;
in vec3 vertexColor;
uniform mat4 projectionMatrix;
uniform mat4 modelMatrix;
out vec3 color;
void main()
{
    gl_Position = projectionMatrix * modelMatrix * vec4(position, 1.0);
    color = vertexColor;
}
"""

FRAGMENT_SHADER = """
in vec3 color;
out vec4 fragColor;
void main()
{
    fragColor = vec4(color, 1.0);
}
"""
