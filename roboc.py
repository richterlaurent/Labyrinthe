from labyrinthe.mapPlayer import *
from labyrinthe.mapReader import *

mr = mapReader()
mapList = mr.readMap('prison')

mp = mapPlayer(mapList)

while not mp.win:
    mp.displayCurrentMap()
    entree = [x for x in input("Votre tour :\n") if x != " "]
    direction = "N"
    moves = 0
    
    try:
        if len(entree) == 1:
            direction = entree[0]
            moves = 1
        else:
            direction = entree[0]
            moves = int("".join(entree[1:]))
    except:
        print("Mauvaise Entrée")
        
    if direction.upper() == "N":
        mp.moveNorth(moves)
    elif direction.upper() == "S":
        mp.moveSouth(moves)
    elif direction.upper() == "W":
        mp.moveWest(moves)
    elif direction.upper() == "E":
        mp.moveEast(moves)
    else:
        print("Mauvaise Entrée")
    
 
mp.displayCurrentMap()   
print("Félicitations! Vous avez gagné!")