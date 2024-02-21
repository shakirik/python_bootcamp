from random import randint

random_num = randint(1,10)
while True:
    guess = int(input("Guess a number between 1 to 10: "))
    if guess < random_num:
        print("Too low")
    elif guess > random_num:
        print("Too high")
    else:
        print("YOU WON")
        play_again = input("Do you want to play again? (y / n): ")
        if play_again == "y":
            random_num = randint(1,10)
            guess = None
        else:
            print("Thanks for playing")
            break
