
class Point3:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    def __str__(self):
        return '(' + ', '.join([str(value) for value in [self.x, self.y, self.z]]) + ')'
    
    def __iter__(self):
        for value in [self.x, self.y, self.z]:
            yield value
    
    def dot(self, v1, v2):
        return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z
        
    def cross(self, v1, v2):
        x = v1.y * v2.z - v1.z * v2.y
        y = v1.x * v2.x - v1.x * v2.z
        z = v1.z * v2.y - v1.y * v2.x
        return Point3(x, y, z)

    def __add__(self, v):
        return Point3(self.x + v.x, self.y + v.y, self.z + v.z)

    def __neg__(self):
        return Point3(-self.x, -self.y, -self.z)

    def __sub__(self, v):
        return self + (-v)
    
    # py3 lol
    def __truediv__(self, other):
        return Point3(self.x / other.x, self.y / other.y, self.z / other.z)

    @classmethod
    def Distance(cls, self, other):
        return ((other.x - self.x)**2 + (other.y - self.y)**2 + (other.z - self.z)**2) **(0.5)
