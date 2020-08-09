
class Vector:
    __init__(self):
        self.x = 0
        self.y = 0

    __init__(self, x, y):
        self.x = x
        self.y = y

    __add__(self, o):
        return Vector(self.x + o.x, self.y + o.y)