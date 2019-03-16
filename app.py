import numpy as np
from mesh import Mesh
from vispy import app, gloo

np.set_printoptions(suppress=True, precision=2)

monkey = Mesh('monkey.obj', position=[1, 2, 3], rotation=[0, 90, 45], scale=[3,3,3])
print(monkey.model_matrix)
print(monkey.position)

canvas = app.Canvas(keys='interactive')

@canvas.connect
def on_draw(event):
    gloo.clear([0.1, 1, 0.5])
    canvas.update()

canvas.show()
app.run()
