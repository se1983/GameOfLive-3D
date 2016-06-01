from OpenGLContext import testingcontext
BaseContext = testingcontext.getInteractive()

from OpenGL.GL import *
from OpenGL.GL import shaders


from OpenGL.arrays import vbo
from OpenGLContext.arrays import *


phong_weightCalc = """
    float phong_weightCalc(
        in vec3 light_pos, // light position
        in vec3 frag_normal // geometry normal
    ) {
        // returns vec2( ambientMult, diffuseMult )
        float n_dot_pos = max( 0.0, dot(
            frag_normal, light_pos
        ));
        return n_dot_pos;
    }
    """

vertex = shaders.compileShader( phong_weightCalc +
"""
uniform vec4 Global_ambient;
uniform vec4 Light_ambient;
uniform vec4 Light_diffuse;
uniform vec3 Light_location;
uniform vec4 Material_ambient;
uniform vec4 Material_diffuse;
attribute vec3 Vertex_position;
attribute vec3 Vertex_normal;
varying vec4 baseColor;
void main() {
    gl_Position = gl_ModelViewProjectionMatrix * vec4(
        Vertex_position, 1.0
    );
    vec3 EC_Light_location = gl_NormalMatrix * Light_location;
    float diffuse_weight = phong_weightCalc(
        normalize(EC_Light_location),
        normalize(gl_NormalMatrix * Vertex_normal)
    );
    baseColor = clamp(
    (
        // global component
        (Global_ambient * Material_ambient)
        // material's interaction with light's contribution
        // to the ambient lighting...
        + (Light_ambient * Material_ambient)
        // material's interaction with the direct light from
        // the light.
        + (Light_diffuse * Material_diffuse * diffuse_weight)
    ), 0.0, 1.0);
}""", GL_VERTEX_SHADER)

"""
vec2 weights = phong_weightCalc(
    normalize(Light_location),
    normalize(Vertex_normal)
);"""

fragment = shaders.compileShader("""
varying vec4 baseColor;
void main() {
    gl_FragColor = baseColor;
}
""", GL_FRAGMENT_SHADER)