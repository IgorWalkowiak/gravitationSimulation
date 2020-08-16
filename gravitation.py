import vector
import math
G_CONST = 15.0

class Gravitation:
    def __init__(self, planets):
        self.planets = planets

    def addPlanet(self, planet):
        self.planets.append(planet)

    def handleCollision(planet, otherPlanet):
        collVector = vector.Vector(otherPlanet.x - planet.x, otherPlanet.y - planet.y)
        cosA = (planet.velocityVector.x*collVector.x + planet.velocityVector.y*collVector.y ) / (planet.velocityVector.getLength()*collVector.getLength())
        alpha = math.acos(cosA)
        newAngle = math.pi-2*alpha
        newVelVector = vector.Vector(planet.velocityVector.x*math.cos(newAngle) - planet.velocityVector.y*math.sin(newAngle),
          planet.velocityVector.x*math.sin(newAngle) + planet.velocityVector.y*math.cos(newAngle))
        planet.velocityVector = newVelVector
        print("_____")
        print(cosA)
        print((collVector.x,collVector.y),(planet.velocityVector.x,planet.velocityVector.y))
        print(alpha)

    def _calculateAcceleration(self, planet):
        sumedForce = (0.0, 0.0)
        for otherPlanet in self.planets:
            if planet == otherPlanet:
                continue
            x = otherPlanet.x - planet.x
            y = otherPlanet.y - planet.y
            rSquared = x*x + y*y
            if planet.radius+otherPlanet.radius >= math.sqrt(rSquared):
                Gravitation.handleCollision(planet, otherPlanet)
                #planet.velocityVector.x = planet.velocityVector.x*(-1)
                #planet.velocityVector.y = planet.velocityVector.y*(-1)
                continue
            simplifiedForce = G_CONST*otherPlanet.mass/rSquared
            sumedForce = (sumedForce[0] + simplifiedForce*x/math.sqrt(rSquared), sumedForce[1] + simplifiedForce*y/math.sqrt(rSquared))
        return (sumedForce[0]/planet.mass, sumedForce[1]/planet.mass)


    def refresh(self, deltaTime):
        for planet in self.planets:
            xAcc, yAcc = self._calculateAcceleration(planet)
            deltaVelocity = vector.Vector(xAcc*deltaTime, yAcc*deltaTime)
            planet.update(deltaVelocity, deltaTime)