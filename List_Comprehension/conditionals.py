numbers = [1, 2, 3, 4, 5, 6, 7]

evens = [nums for nums in numbers if nums % 2 == 0]
odds = [nums for nums in numbers if nums % 2 != 0]

print(evens)
print(odds)