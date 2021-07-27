import random
import pandas as pd
import matplotlib.pyplot as plt


def play_rps():

    rps_tries = 0
    rps_score = 0
    rps_playagain = 0
    rps_username = input("Enter your name: ")

    def append_csv_and_read_from_it_rps():

        playersRPS = {rps_username: rps_score}

        playerDataRPS = pd.DataFrame(playersRPS, index=playersRPS.keys())

        playerDataRPS.to_csv("rps_scorelist.csv", header=None, mode="a")

        colsRPS = ["Username", "Score"]

        playerDatatoPlotRPS = pd.read_csv(
            "rps_scorelist.csv", names=colsRPS, header=None)

        playerDatatoPlotRPS.set_index("Username")

        playerDatatoPlotRPS.plot(kind="bar", x="Username", y="Score")

    while rps_tries < 5:

        print('Make your choice:')
        choice = str(input())
        choice = choice.lower()

        print("My choice is", choice)

        choices = ['rock', 'paper', 'scissors']

        computer_choice = random.choice(choices)
        print(computer_choice)

        print("Computer choice is", computer_choice)
        if choice in choices:
            if choice == computer_choice:
                print('it is a tie')
                rps_tries += 1
                print(rps_score)
            if choice == 'rock':
                if computer_choice == 'paper':
                    print('you lose, sorry :(')
                    rps_score -= 10
                    rps_tries += 1
                    print(rps_score)
                elif computer_choice == 'scissors':
                    print('You win!!!!! congrats :)')
                    rps_score += 10
                    rps_tries += 1
                    print(rps_score)
            if choice == 'paper':
                if computer_choice == 'scissors':
                    print('you lose, sorry :(')
                    rps_score -= 10
                    rps_tries += 1
                    print(rps_score)
                elif computer_choice == 'rock':
                    print('You win!!!!! congrats :)')
                    rps_score += 10
                    rps_tries += 1
                    print(rps_score)
            if choice == 'scissors':
                if computer_choice == 'rock':
                    print('you lose, sorry :(')
                    rps_score -= 10
                    rps_tries += 1
                    print(rps_score)
                elif computer_choice == 'paper':
                    print('You win!!!!! congrats :)')
                    rps_score += 10
                    rps_tries += 1
                    print(rps_score)

        else:
            print('invalid choice, try again')

        if rps_tries == 5:
            print("You have run out of tries")

            showPlotRPS = input("Do you want to see the bar chart? (y/n) ")
            if showPlotRPS.lower() == "y":
                append_csv_and_read_from_it_rps()
                plt.show()
                break
            elif showPlotRPS.lower() == "n":
                append_csv_and_read_from_it_rps()
                print("Thanks for playing. Goodbye!")
                break

            else:
                print("Invalid Input!")
                break


# play_rps()
