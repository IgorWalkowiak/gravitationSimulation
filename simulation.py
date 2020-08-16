import board
import planet
import gravitation
import vector

pl1 = planet.Planet(10,550,400,200,(100,0,255),vector.Vector(0,0.1))
pl2 = planet.Planet(10,800,400,200,(100,0,255),vector.Vector(0,0))
#pl3 = planet.Planet(20,750,400,1000,(0,202,0), vector.Vector(0,0))

planets = [pl1, pl2]# ]#pl3]

grav = gravitation.Gravitation(planets)
board = board.Board(planets)

while True:
    board.print()
    grav.refresh(0.5)