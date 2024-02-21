# slicing is [start:end:step]

first_list = [1, 2, 3, 4]

print(first_list[2:])
print(first_list[:3])

print(first_list[:-1])
print(first_list[2:-1])
print(first_list[::-1])


# swapping values 

names = ["Shakir", "Kabir"]

names[0], names[1] = names[1], names[0]
print(names)