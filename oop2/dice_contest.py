#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Running a simulation with our classes"""

# import our classes
from cheatdice import *

def main():
    """called at runtime"""

    # the player known as the swapper
    player1 = Cheat_Swapper()
    # the player known as the loaded_dice
    player2 = Cheat_Loaded_Dice()

    # track scores for both players
    player1_score = 0
    player2_score = 0

    # how many games we want to run
    number_of_games = 100000
    game_number = 0

    # begin!
    print("Simulation running")
    print("==================")
    while game_number < number_of_games:
        player1.roll()
        player2.roll()

        player1.cheat()
        player2.cheat()
        """Remove # before print statements to see simulation running
           Simulation takes approximately one hour to run with print
           statements or ten seconds with print statements
           commented out"""

        #print("Cheater 1 rolled" + str(swapper.get_dice()))
        #print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
        if sum(player1.get_dice()) == sum(player2.get_dice()):
            #print("Draw!")
            pass
        elif sum(player1.get_dice()) > sum(player2.get_dice()):
            #print("Dice swapper wins!")
            player1_score+= 1
        else:
            #print("Loaded dice wins!")
            player2_score += 1
        game_number += 1

    # the game has ended
    print("Simulation complete")
    print("-------------------")
    print("Final scores")
    print("------------")
    print(f"Player1 won: {player1_score}")
    print(f"Player2 won: {player2_score}")

    # determine the winner
    if player1_score == player2_score:
        print("Game was drawn")
    elif player1_score > player2_score:
        print("Player1 won most games")
    else:
        print("Player2 won most games")

if __name__ == "__main__":
    main()

