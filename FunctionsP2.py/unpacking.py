def sum_of_nums (*args):
    print(type(nums))
    total = 0
    for num in args:
        total += num
    print(total)

nums = [1, 2, 4, 5, 6, 7]
sum_of_nums(*nums)

# this is to unpack tuples or lists

# ** to unpack dicts