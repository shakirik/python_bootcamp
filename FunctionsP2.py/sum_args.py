def sum_of_nums (*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(sum_of_nums(2, 3, 5, 6, 4,3,6))
print(sum_of_nums(2, 4))