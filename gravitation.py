G_CONST = 0.5

class Gravitation:
    def __init__(self):
        self.planets = []

    def addPlanet(self, planet):
        self.planets.append(planet)

    def _calculateAcceleration(self, planet):
        calcAcceleration = (0.0, 0.0)
        for otherPlanet in planets:
            if planet == otherPlanet:
                continue
            x = otherPlanet.x - planet.x
            y = otherPlanet.y - planet.y
            if x>0:
                if y>0:
                    calcAcceleration = (calcForce[0] + G_CONST*otherPlanet.mass/(x*x), calcForce[1] + G_CONST*otherPlanet.mass/(y*y))
                else:
                    calcAcceleration = (calcForce[0] + G_CONST*otherPlanet.mass/(x*x), calcForce[1] - G_CONST*otherPlanet.mass/(y*y))
            else:
                if y>0:
                    calcAcceleration = (calcForce[0] - G_CONST*otherPlanet.mass/(x*x), calcForce[1] + G_CONST*otherPlanet.mass/(y*y))
                else:
                    calcAcceleration = (calcForce[0] - G_CONST*otherPlanet.mass/(x*x), calcForce[1] - G_CONST*otherPlanet.mass/(y*y))
        return calcAcceleration


    def refresh(self, deltaTime):
        for planet in self.planets:
            xAcc, yAcc = self._calculateAcceleration(planet)
            deltaVelocity = Vector(xAcc*deltaTime, yAcc*deltaTime)
            planet.addVelocity(deltaVelocity)

