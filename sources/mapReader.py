'''
Created on 7 sept. 2016

This module establishes the whole "reading" communication with the map.

@author: Richter
'''
import os

def importMaps():
    ''' Function that import the maps from the maps diectory :
    @param : none
    @preturn : list of maps files
    '''
    maps = os.listdir('../cartes')
    mapNames = []
    for map in maps:
        mapNames.extend(map.split("."))
    mapNames = [m for m in mapNames if m != 'txt']
    return maps


def readMap(map):
    '''
        This function reads the map in parameter and displays it
        @param : the map name
        @return : the map display
    '''
    fileAccess = '../cartes/' + map + '.txt'
    with open(fileAccess, 'r') as file:
        print(file.read())