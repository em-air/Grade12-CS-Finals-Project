import random
import pandas as pd
import matplotlib.pyplot as plt


def play_gg():
    ranNum = random.randint(1, 10)
    tries = 0
    score = 50
    username = input("Enter your name: ")
    print(ranNum)

    def append_csv_and_read_from_it():
    
        players = {username: score}
        playerData = pd.DataFrame(players, index=players.keys())

        playerData.to_csv("scorelist.csv", header=None, mode="a")
        cols = ["Username", "Score"]
        
        playerDatatoPlot = pd.read_csv(
            "scorelist.csv", names=cols, header=None)

        playerDatatoPlot.set_index("Username")

        playerDatatoPlot.plot(kind="bar", x="Username", y="Score")
        

    print(
        f"Hello {username}, Welcome to the guessing game. "
        f"A random number has been chosen between 1 and 10 and you have"
        f" 5 tries to guess it."
    )
    while tries < 6:
        userInput = int(input("Enter a guess: "))
        if userInput > ranNum:
            print(
                f"Wrong! The right answer is less than {userInput}. Try again.")
            tries += 1
            score -= 10  # score decreases with the number of tries
        elif userInput < ranNum:
            print(
                f"Wrong! The right answer is more than {userInput} . Try again.")
            tries += 1
            score -= 10  # score decreases with the number of tries
        elif userInput == ranNum:
            print(f"You got it right. It took you {tries} tries to get it.")
            print(f'Your score is {score}')
            showPlot = input("Do you want to see the bar chart? (y/n) ")
            if showPlot.lower() == "y":
                append_csv_and_read_from_it()
                plt.show()
                break
            elif showPlot.lower() == "n":
                append_csv_and_read_from_it()
                print("Thanks for playing. Goodbye!")
                break
            else:
                print("Invalid Input!")
                break
        if tries == 5:
            append_csv_and_read_from_it()
            print(f"Your score is {score}")
            print(
                "You have run out of tries and you've lost the game. Thanks for playing! Goodbye..")
            break

# play_gg()
