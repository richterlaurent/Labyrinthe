from game import Game


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





































