#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5
# -*-coding:utf-8 -*
'''
Created on 7 sept. 2016

This module establishes the whole reading communication with the map.

@author: Richter
'''
import os


def singleton(classe_definie):
    instances = {} # Dictionnaire de nos instances singletons
    def get_instance():
        if classe_definie not in instances:
            # On crée notre premier objet de classe_definie
            instances[classe_definie] = classe_definie()
        return instances[classe_definie]
    return get_instance


@singleton
class mapReader():
    
    @staticmethod
    def importMaps():
        ''' Function that import the maps from the maps diectory :
            @param : none
            @preturn : list of maps files
        '''
        maps = os.listdir('cartes')
        mapNames = []
        for m in maps:
            mapNames.extend(m.split("."))
        mapNames = [el for el in mapNames if el != 'txt']
        return maps
    
    @staticmethod
    def readMap(mapName):
        '''
            This function reads the map in parameter and displays it
            @param : str (map name)
            @return : list (map content)
        '''
        fileAccess = 'cartes/' + mapName
        with open(fileAccess, 'r') as file:
            return list(file.read())
    
    @staticmethod
    def isTmpMap():
        if len(os.listdir('tmp')) > 1:
            return True
        else:
            return False
            
      
    @staticmethod        
    def readTmpMap():
        '''
            This function returns the map stored in the 'tmp' folder if it exists
            and a boolean that indicates if it exists or not
            @param : None
            @return : Boolean, List (map containing)
        '''
        try:
            with open('tmp/mapTmp.txt', 'r') as tmpFile:
                return list(tmpFile.read())
        except:
            print("Erreur à l'ouverture de la partie en cours")
            return None

    @staticmethod
    def saveMap(mapContent):
        '''
            This method saves the list in parameter in the 'tmp' folder
            as a 'mapTmp.txt' file
            
            @param : list (map to save)
            @return: None 
        '''
        mapText = "".join(mapContent)
        with open('tmp/mapTmp.txt', 'w') as mapTmp:
            mapTmp.write(mapText)
        
    
    
    @staticmethod
    def displayMap(mapContent):
        '''
            This method displays the map entered as a list in parameter
            @param : the list representing the map
            @return : None (print the map directly)
        '''
        mapAsTxt = "".join(mapContent)
        print(mapAsTxt)

    @staticmethod
    def deleteTmp():
        os.remove('tmp/mapTmp.txt')
        










