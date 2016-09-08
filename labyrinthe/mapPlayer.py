#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
# -*-coding:utf-8 -*

class mapPlayer():
    
    def __init__(self, mapList):
        self.mapList = mapList
        self._lineLength = mapList.index("\n") + 1
        self.door = False
        self.win = False
        
        
    def moveNorth(self, moves):
        '''
            The method moves the position to the north,
            depending on the number of moves
            @param : int
            @return : list (the new map as list)
        '''
        currPos = self.mapList.index("X")
        previous = currPos
        ok = True
                
        for i in range(1,moves+1):

            if ok and not self.win and (currPos - self._lineLength * i) > self._lineLength :
                
                if self.mapList[currPos - (self._lineLength * i)] == " ":
                    if self.door:
                        self.mapList[previous] = "."
                    else:
                        self.mapList[previous] = " "            
                    self.mapList[currPos - (self._lineLength * i)] = "X"
                    previous = currPos - self._lineLength * i
                    self.door = False                
                elif self.mapList[currPos - (self._lineLength * i)] == ".":
                    self.mapList[previous] = " "
                    self.mapList[currPos - (self._lineLength * i)] = "X"
                    previous = currPos - self._lineLength * i
                    self.door = True                                      
                elif self.mapList[currPos - (self._lineLength * i)] == "U":
                    self.mapList[previous] = " "
                    self.mapList[currPos - self._lineLength * i] = "W" 
                    self.win = True
                else:
                    ok = False
        return self.mapList
    
    
    def moveSouth(self, moves):
        '''
            The method moves the position to the south,
            depending on the number of moves
            @param : int
            @return : None
        '''
        currPos = self.mapList.index("X")
        previous = currPos
        ok = True        
        
        for i in range(1,moves+1):
            
            if ok and not self.win and (currPos + self._lineLength * i) < len(self.mapList) - self._lineLength :
                
                if self.mapList[currPos + (self._lineLength * i)] == " ":
                    if self.door:
                        self.mapList[previous] = "."
                    else:
                        self.mapList[previous] = " "            
                    self.mapList[currPos + (self._lineLength * i)] = "X"
                    previous = currPos + self._lineLength * i
                    self.door = False                
                elif self.mapList[currPos + (self._lineLength * i)] == ".":
                    self.mapList[previous] = " "
                    self.mapList[currPos + (self._lineLength * i)] = "X"
                    previous = currPos + self._lineLength * i
                    self.door = True                                      
                elif self.mapList[currPos + (self._lineLength * i)] == "U":
                    self.mapList[previous] = " "
                    self.mapList[currPos + self._lineLength * i] = "W"
                    self.win = True
                else:
                    ok = False
                    
        return self.mapList
    
    
    
    def moveWest(self, moves):
        '''
            The method moves the position to the west,
            depending on the number of moves
            @param : int
            @return : None
        '''
        currPos = self.mapList.index("X")
        previous = currPos
        ok = True        
        
        for i in range(1,moves+1):
            
            if ok and not self.win :
                
                if self.mapList[currPos - i] == " ":
                    if self.door:
                        self.mapList[previous] = "."
                    else:
                        self.mapList[previous] = " "            
                    self.mapList[currPos - i] = "X"
                    previous = currPos - i
                    self.door = False                
                elif self.mapList[currPos - i] == ".":
                    self.mapList[previous] = " "
                    self.mapList[currPos - i] = "X"
                    previous = currPos - i
                    self.door = True                                      
                elif self.mapList[currPos - i] == "U":
                    self.mapList[previous] = " "
                    self.mapList[currPos - i] = "W"
                    self.win = True
                else :
                    ok = False
                    
        return self.mapList
    
    def moveEast(self, moves):
        '''
            The method moves the position to the east,
            depending on the number of moves
            @param : int
            @return : None
        '''
        currPos = self.mapList.index("X")
        previous = currPos
        ok = True        
        
        for i in range(1,moves+1):
            
            if ok and not self.win:
                
                if self.mapList[currPos + i] == " ":
                    if self.door:
                        self.mapList[previous] = "."
                    else:
                        self.mapList[previous] = " "            
                    self.mapList[currPos + i] = "X"
                    previous = currPos + i
                    self.door = False                
                elif self.mapList[currPos + i] == ".":
                    self.mapList[previous] = " "
                    self.mapList[currPos + i] = "X"
                    previous = currPos + i
                    self.door = True                                      
                elif self.mapList[currPos + i] == "U":
                    self.mapList[previous] = " "
                    self.mapList[currPos + i] = "W" 
                    self.win = True
                else:
                    ok = False
                    
        return self.mapList
        
        
    def displayCurrentMap(self):
        print("".join(self.mapList))
        
        
        
        
        
        