from mapReader import mapReader
from mapPlayer import mapPlayer

class Game():
    '''
        Game class : establishes the whole gaming connection
        with the mapReader and the mapPlayer class
        The whole logic of the game is in this file. 
    '''
    
    def __init__(self):
        self.mr = mapReader()
        self.mp = None
        self.map = None
        self.quit = False
        self.win = False
    
    
    def displayMaps(self):
        '''
            This method displays the maps available
            and ask the player to choose. 
            The map is loaded in the self.map attribute
            @param: None
            @return: None
        '''
        maps = self.mr.importMaps()
        availableChoices = []
        print("Labyrinthes existants :")
        for i, m in enumerate(maps):
            availableChoices.append(i+1)
            print("  {0}  -  {1}".format(i+1, m[:-4]))
            
        choice = "X"
        while not choice.isnumeric():
            while choice not in str(availableChoices):
                choice = input("Entrez votre choix : ")
        
        choice = int(choice)
        self.map = self.mr.readMap(maps[choice - 1])
        self.mp = mapPlayer(self.map)
        
        
            
    def tmpMapAvailable(self):
        '''
            This method shows a message if a game is already open
            and asks if the player wants to continue
            @param: None
            @return: Boolean
        '''
        if self.mr.isTmpMap():
            print("Une partie est toujours en cours.\nVoulez-vous la continuer ?")
            choice = "X"
            while choice not in ["O","N"]:
                choice = input("O/N : ").upper()
            if choice == "O":
                self.map = self.mr.readTmpMap()
                self.mp = mapPlayer(self.map)
                return True
            else:
                return False
                        
    
    def playMoves(self):
        '''
            The method to play the Game
            @prama: None
            @return: Boolean (if win or not)
        '''
        self.win = False
        while not self.mp.win and not self.quit:
            self.mp.displayCurrentMap()
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
                self.mp.moveNorth(moves)
            elif direction.upper() == "S":
                self.mp.moveSouth(moves)
            elif direction.upper() == "W":
                self.mp.moveWest(moves)
            elif direction.upper() == "E":
                self.mp.moveEast(moves)
            elif direction.upper() == "Q":
                self.quit = True
            else:
                print("Mauvaise Entrée")

            self.mr.saveMap(self.mp.mapList)
     
            if self.mp.win:
                self.mr.deleteTmp()
                self.win = self.mp.win
     
        
    def titleMessage(self):
        '''
            This method displays a message at the start of the game
            @param: None
            @return: None
        '''
        print("----------------------")
        print("----- Labyrinthe -----")
        print("----------------------")
       
    
    def winDisplay(self):
        '''
            Prints a message if win
            @param: None
            @return: None
        '''
        self.mp.displayCurrentMap()
        print("Félicitions! Vous avez gagné!\n")
        
          
    def outputDisplay(self):
        '''
            Displays a message when quiting
            @param: None
            @return: None
        '''
        print("Merci d'avoir joué avec nous.\nA la prochaine !\n")     
            
            
            
            
            
            
            
            
            
            
            
            
            
            