numbers = [2, 483, 29203, 4, 18]

doublednumbers = [num*2 for num in numbers if num % 2 == 0]
print(doublednumbers)

falsevalues = [False, "", []]
checker = [bool(val) for val in falsevalues]
print(checker)



timesby10numbers = [num*10 for num in range(0,6)]
print(timesby10numbers)