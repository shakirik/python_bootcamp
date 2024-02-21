# state vs global (code that is somewhere else oustide of your function)
# nonlocal (can modify a parent's variable in a childs function) for nested functions


total = 2 

def increment ():
    global total
    total += 1
    return total

print(increment())