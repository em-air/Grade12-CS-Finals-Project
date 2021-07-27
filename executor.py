import guessing_game
import rps

chooseGame = input('''What game would you like to play?
                             1. Guessing Game
                             2. Rock Paper Scissors
                             Enter: ''')

if chooseGame == "gg":
     guessing_game.play_gg()
elif chooseGame == "rps":
     rps.play_rps()
     