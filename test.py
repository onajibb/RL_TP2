from Game import Game 

game = Game(m=4, n=4)
game.generate_game()

print(game.reset())
print(game._position_to_id(game.position[0], game.position[1]))

print(game.move(1))

import random
print(random.random())