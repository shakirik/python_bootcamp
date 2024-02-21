from random import randint
player_wins = 0
computer_wins = 0


print("Rock...")
print("Paper...")
print("Scissors...")
print(f"Starting Scores: Player Score: {player_wins} -- Computer Score: {computer_wins}")

while player_wins < 2 and computer_wins < 2:
    player = input("Player, make your move: ").lower()
    if player == "quit" or player == "q":
        break
    rand_num = randint(0,2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"

    print(f"Computer plays {computer}" )

    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("player wins!")
            player_wins += 1
        else:
            print("computer wins!")
            computer_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("player wins!")
            player_wins += 1
        else:
            print("computer wins!")
            computer_wins += 1

    elif player == "scissors":
        if computer == "paper":
            print("player wins!")
            player_wins += 1
        else:
            print("computer wins!")
            computer_wins += 1
    else:
        print("Please enter a valid move!")
        
        
print(f"Final Scores: Player Score: {player_wins} -- Computer Score: {computer_wins}")
if player_wins > computer_wins:
    print("CONGRATS, YOU WON!")
elif player_wins == computer_wins:
    print("IT'S A TIE")
else: 
    print("OH NO :( THE COMPUTER WON...")