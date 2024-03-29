import numpy as np
from mesh import Mesh
from vispy import app, gloo
from vispy.util import transforms as tr

np.set_printoptions(suppress=True, precision=2)

VERT_SHADER = """
attribute vec3 vertex;
uniform mat4 model_matrix;
uniform mat4 projection_matrix;
void main(){
    gl_Position = model_matrix * vec4(vertex, 1);
}
"""

FRAG_SHADER = """
void main(){
    gl_FragColor = vec4(1., 0., 0., 1.);
}
"""

program = gloo.Program(VERT_SHADER, FRAG_SHADER)


monkey = Mesh('monkey.obj', position=[1, 0, 1], rotation=[45, 90, 45], scale=[1,1,1])
print(monkey.model_matrix)
print(monkey.position)

projection_matrix = tr.perspective(90, 1.33, .1, 20)
program['projection_matrix'] = projection_matrix

attributes = [
    ('vertex', np.float32, 3)
]

data = np.zeros(len(monkey.vertices), attributes)
data['vertex'] = monkey.vertices
vertex_buffer = gloo.VertexBuffer(data)
program.bind(vertex_buffer)

index_buffer = gloo.IndexBuffer(monkey.faces)

canvas = app.Canvas(keys='interactive')

@canvas.connect
def on_draw(event):
    monkey.rotation[1] += .1
    program['model_matrix'] = monkey.model_matrix
    gloo.clear([0.1, 0.8, 1])
    program.draw('triangles', index_buffer)
    canvas.update()

canvas.show()
app.run()
