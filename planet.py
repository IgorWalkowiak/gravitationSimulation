import vector

class Planet:

    def __init__(self, radius, x, y, mass, color, velocityVector = vector.Vector(0,0)):
        self.velocityVector = velocityVector
        self.color = color
        self.radius = radius
        self.x = x
        self.y = y
        self.mass = mass

    def update(self, velocityVectorChange, deltaTime):
        self.velocityVector = self.velocityVector + velocityVectorChange
        self.x = self.x + self.velocityVector.x * deltaTime
        self.y = self.y + self.velocityVector.y * deltaTime