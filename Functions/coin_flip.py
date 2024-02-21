from random import randint   

def flip_coin ():
    r = randint(0,2)
    if r > 0:
        return "HEADS"
    else:
        return "Tails"

print(flip_coin())      