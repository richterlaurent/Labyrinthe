# -*-coding:utf-8 -*

from game import Game

'''
    roboc.py instantiates the Game object and handles 
    the main steps via this same object	
'''


game = Game()
game.titleMessage()

if game.tmpMapAvailable():
    pass
else:
    game.displayMaps()   
game.playMoves()
if game.win:
    game.winDisplay()


game.outputDisplay()





































