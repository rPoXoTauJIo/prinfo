
# cretids to Tatsuya Yatagawa 
# copypasted&modified from https://gist.github.com/tatsy/e14dd18079bca60ac8f78217b77332c1

import math

class Point3d(object):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def dot(v1, v2):
        return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

    @staticmethod
    def cross(v1, v2):
        x = v1.y * v2.z - v1.z * v2.y
        y = v1.x * v2.x - v1.x * v2.z
        z = v1.z * v2.y - v1.y * v2.x
        return Point3d(x, y, z)

    @staticmethod
    def normalize(v):
        return v / v.norm()

    def norm(self):
        return math.sqrt(Point3d.dot(self, self))

    def __add__(self, v):
        return Point3d(self.x + v.x, self.y + v.y, self.z + v.z)

    def __neg__(self):
        return Point3d(-self.x, -self.y, -self.z)

    def __sub__(self, v):
        return self + (-v)

    def __str__(self):
        return '(%.4f, %.4f, %.4f)' % (self.x, self.y, self.z)

    @classmethod
    def Distance(cls, v1, v2):
        return ((v2.x - v1.x)**2 + (v2.y - v1.y)**2 + (v2.z - v1.z)**2) **(0.5)