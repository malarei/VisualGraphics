#import numpy as np
#from vispy.util import transforms as tr

#np.set_printoptions(suppress=True, precision=2)

#def make_model_matrix(translate, rotation, scale):
#     """
#     Returns a 4x4 model matrix
#
#     Arguments:
#         -translation: x, y, z coordinates
#         -rotation: z rotation (degrees)
#         -scale: x, y, z scale
#
# Returns:
#         -model_matrix: 4x4 array
#     """
#    sm = tr.scale(scale).T
#    rz = rotation
#    rzm =tr.rotate(rz, [0,0,1]).T
#    trm = tr.translate(translate).T
#    mm = trm @ rzm @ sm
#    return mm

#print('Hello')

#mm = make_model_matrix([2,6,8],[45],[3,3,3])
#print(mm)

import numpy as np
from vispy import io
from vispy.util import transforms as tr

np.set_printoptions(suppress=True, precision=2)

class Mesh:

    def __init__(self, obj_filename, position, rotation, scale):  #def is a new function
        vertices, faces, normals, texcoords = io.read_mesh(obj_filename)
        assert len(vertices[0]) == 3, "Vertices r 3D"
        assert len(faces[0]) == 3, "Mesh must be triangulated"
        self.vertices = vertices
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
            mm = trm @ rxm @rym @rzm @ sm
            return mm
#@property
#def position(self):
    return self._position  #_ is private

#@position.setter
#def position(self, value):
#    self._position = value
#    self.model_matrix = make_model_matrix(self.position, self.rotation, self.scale)

#@property
#    def rotation(self):
#        return self._rotation  #_ is private

#@rotation.setter
#    def rotation(self, value):
#        self._rotation = value
#        self.model_matrix = make_model_matrix(self.position, self.rotation, self.scale)

#@property
#def get_scale(self):
#    return self._scale  #_ is private

#@scale.setter
#def position(self, value):
#    self._scale = value
#    self.model_matrix = make_model_matrix(self.position, self.rotation, self.scale)


monkey = Mesh('monkey.obj', position=[1, 2, 3], rotation=[0, 90, 45], scale=[3,3,3])
#print(monkey.vertices)
#print(monkey.faces)
#monkey.position
print(monkey.model_matrix)
#monkey.send()
#monkey.draw()

mm = make_model_matrix([2,6,8], [0, 90, 45], [3,3,3])
print(mm)

#vertices, faces, normals, texcoords = io.read_mesh('monkey.obj')
#read_mesh()
#print(len(vertices[0]))
#assert len(vertices[0]) == 3, "Vertices r 3D"
#assert len(faces[0]) == 3, "Mesh must be triangulated"
