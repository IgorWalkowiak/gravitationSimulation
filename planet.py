import vector

class Planet:

    def __init__(self, radius, x, y, velocityVector):
        self.velocityVector = velocityVector
        self.radius = radius
        self.position = (x, y)
        self.mass = 1.0

    def addVelocity(self, velocityVectorChange)
        self.velocityVector = self.velocityVector + velocityVectorChange