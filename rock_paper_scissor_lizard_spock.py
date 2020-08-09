""""
The rules are:
Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock
Rock crushes Scissors
"""
import random

user_point = 0
comp_point = 0
n = int(input("Number of times the game is to be played\n"))

while (n):
    print("Enter the choice")

    user_choice = input()
    print("User Choice is:",user_choice)

    list_of_game_choice = ['rock','paper','scissor','lizard','spock']

    computer_choice = random.choice(list_of_game_choice)
    print("Computer choice is:",computer_choice)

    if user_choice in list_of_game_choice:

        if user_choice == computer_choice:
            print("It is a tie")

        if user_choice == 'rock' and (computer_choice == 'scissor' or computer_choice == 'lizard'):
                print("User wins")
                user_point += 1
        elif user_choice == 'rock' and (computer_choice == 'paper' or computer_choice == 'spock'):
                print("Computer wins")
                comp_point += 1

        if user_choice == 'paper' and (computer_choice == 'rock' or computer_choice == 'spock'):
                print("User wins")
                user_point += 1
        elif user_choice == 'paper' and (computer_choice == 'scissor' or computer_choice == 'lizard'):
                print("Computer wins")
                comp_point += 1

        if user_choice == 'scissor' and (computer_choice == 'paper' or computer_choice == 'lizard'):
                print("User wins")
                user_point += 1
        elif user_choice == 'scissor' and (computer_choice == 'rock' or computer_choice == 'spock'):
                print("Computer wins")
                comp_point += 1

        if user_choice == 'lizard' and (computer_choice == 'spock' or computer_choice == 'paper'):
                print("User wins")
                user_point += 1
        elif user_choice == 'lizard' and (computer_choice == 'scissor' or computer_choice == 'rock'):
                print("Computer wins")
                comp_point += 1

        if user_choice == 'spock' and (computer_choice == 'rock' or computer_choice == 'scissor'):
                print("User wins")
                user_point += 1
        elif user_choice == 'spock' and (computer_choice == 'lizard' or computer_choice == 'paper'):
                print("Computer wins")
                comp_point += 1

    else:
        print("Invalid choice restart the game")

    print()
    n=n-1

if (user_point > comp_point):
    print("User wins:",user_point)
elif (user_point == comp_point):
    print("Draw")
else:
    print("Computer wins:",comp_point)