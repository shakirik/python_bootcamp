print("rock...")
print("scissors...")
print("paper...")

player1 = input("Player 1, Make your move: ")
player2 = input("Player 2, Make your move: ")

if player1 == "rock" and player2 == "scissors":
    print("player1 wins!")
elif player1 == "rock" and player2 == "paper":
    print("player2 wins")
elif player1 == player2:
    print("Its a tie")




