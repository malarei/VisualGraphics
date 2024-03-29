import numpy as np
from vispy import io
from vispy.util import transforms as tr

np.set_printoptions(suppress=True, precision=2)

class Mesh:

    def __init__(self, obj_filename, position, rotation, scale):  #def is a new function
        vertices, faces, normals, texcoords = io.read_mesh(obj_filename)
        assert len(vertices[0]) == 3, "Vertices r 3D"
        assert len(faces[0]) == 3, "Mesh must be triangulated"
        self.vertices = vertices - np.mean(vertices, axis=0)
        self.faces = faces
        self.position = position
        self.rotation = rotation
        self.scale = scale

    @property
    def model_matrix(self):
            """
            Returns a 4x4 model matrix

            Arguments:
                -translation: x, y, z coordinates
                -rotation: z rotation (degrees)
                -scale: x, y, z scale

            Returns:
                -model_matrix: 4x4 array
            """
            sm = tr.scale(self.scale).T
            rx, ry, rz = self.rotation
            rxm =tr.rotate(rx, [1,0,0]).T
            rym =tr.rotate(ry, [0,1,0]).T
            rzm =tr.rotate(rz, [0,0,1]).T
            trm = tr.translate(self.position).T
            mm = trm @ rxm @ rym @ rzm @ sm
            return mm
