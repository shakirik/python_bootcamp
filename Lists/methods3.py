# Index, Count, Sort, Reverse and Join

examplecount = ["Shakir", "Kabir", "Josh", "Bron"]
print(examplecount.count("Shakir"))
print(examplecount.count("Shak"))

examplereverse = ["Shakir", "Kabir", "Josh", "Bron"]
examplereverse.reverse()
print(examplereverse)

examplesort = [1, 3, 6, 2, 4, 9, 7]
examplesort.sort()
print(examplesort)

seperator = " "
names = ["Shakir", "Islam", "Kabir"]
full_name = seperator.join(names)
print(full_name)