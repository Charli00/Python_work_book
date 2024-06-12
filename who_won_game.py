import random
from getpass import getpass as input

print("Rock, Paper, Scissors")
print()
print("Select your move (R, P, or S)")
print()

player1_score = 0
player2_score = 0

while True:
    a = input("Player1> (R, P, S): ").strip().upper()
    b = input("Player2> (R, P, S): ").strip().upper()

    if a not in ['R', 'P', 'S'] or b not in ['R', 'P', 'S']:
        print("Invalid input. Please enter R, P, or S.")
        continue

    if a == b:
        print("It's a tie")
    elif (a == "R" and b == "P") or (a == 'S' and b == 'R') or (a == 'P' and b == 'S'):
        print("Player2 wins")
        player2_score += 1
    elif (a == "R" and b == "S") or (a == 'S' and b == 'P') or (a == 'P' and b == 'R'):
        print("Player1 wins")
        player1_score += 1

    print(f"Score: Player1 - {player1_score}, Player2 - {player2_score}")

    affirmation = input("Do you want to play another round? (Y/N): ").strip().upper()
    if affirmation != 'Y':
        print("Final Score:")
        print(f"Player1: {player1_score}")
        print(f"Player2: {player2_score}")
        if player1_score > player2_score:
            print("Player1 is the overall winner!")
        elif player1_score < player2_score:
            print("Player2 is the overall winner!")
        else:
            print("It's a tie overall!")
        break
