import random

choices = ["Rock", "Paper", "Scissors"]


# finish_game = False
player_score = 0
computer_score = 0

while(True):
    computer = random.choice(choices)
    player = ""

    answer = input("Please select one of the options (P - Paper, R - Rock, S - Scissors, Q - Quit Game): ")
    if answer == 'P' or answer == 'p':
        player = choices[1]
    elif answer == 'R' or answer == 'r':
        player = choices[0]
    elif answer == 'S' or answer == 's':
        player = choices[2]
    elif answer == 'Q' or answer == "q":
        print("Goodbye")
        break
    else:
        print("There is no such option")
        continue

    if (computer == player):
        print("Computer: " + computer + " - Player: " + player)
        # print("Result: Draw")
        computer_score += 1
        player_score += 1
        print("Score: " + str(computer_score) + " - " + str(player_score))
        # print("Result: Draw")
    elif ((computer == "Rock" and player == "Scissors") or
          (computer == "Scissors" and player == "Paper") or
          (computer == "Paper" and player == "Rock")):
        print("Computer: " + computer + " - Player: " + player)
        # print("Result: Computer wins")
        computer_score += 1
        print("Score: " + str(computer_score) + " - " + str(player_score))
    else:
        print("Computer: " + computer + " - Player: " + player)
        # print("Result: You win")
        player_score += 1
        print("Score: " + str(computer_score) + " - " + str(player_score))

if computer_score == player_score and computer_score != 0:
    print("Result: Draw")
if computer_score > player_score:
    print("Result: Computer wins")
if computer_score < player_score:
    print("Result: You win")
